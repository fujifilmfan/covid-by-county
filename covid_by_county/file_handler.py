#!/usr/bin/env python

import asyncio
from datetime import date, timedelta
from pathlib import Path

import aiohttp
from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectTimeout, ConnectionError

import covid_by_county.config as app_config

config = app_config.configuration


class FileHandler:

    def __init__(
            self,
            raw_data_dir=config.raw_data_dir,
            processed_data_dir=config.processed_data_dir,
            reference_data_dir=config.reference_data_dir,
            png_dir=config.png_dir,
            start_date=config.start_date):
        self.raw_data_dir = raw_data_dir
        self.raw_data_paths = self.raw_data_dir.iterdir()
        self.processed_data_dir = processed_data_dir
        self.reference_data_dir = reference_data_dir
        self.png_dir = png_dir
        self.start_date = start_date
        # self._check_dirs()
        self.local_raw_csvs = self._find_local_raw_csvs()
        self.index_url = config.source_data_index_url
        self.download_url = config.source_data_download_url
        self.figure_creator = config.figure_creator

    def create_data_dirs(self):
        """Create default data and image directories.

        :return: None
        """

        if not self.raw_data_dir.is_dir():
            self._create_dir(self.raw_data_dir)
        if not self.processed_data_dir.is_dir():
            self._create_dir(self.processed_data_dir)
        if not self.reference_data_dir.is_dir():
            self._create_dir(self.reference_data_dir)
        if not self.png_dir.is_dir():
            self._create_dir(self.png_dir)

    @staticmethod
    def _create_dir(path):
        """Create a directory.

        :param path: OBJ; Path object specifying path to create
        :return: None
        """

        path.mkdir()

    def _create_file_set(self):
        """Create a set of possible file names based on start date.

        This function takes start_date as a tuple, converts it into a
        datetime.date object, and then creates a set of files based on
        the dates between that start date and today, inclusive.

        :return: SET; file names formatted like '02-14-2020.csv'
        """

        year, month, day = self.start_date
        start_date = date(year, month, day)
        end_date = date.today()
        delta = end_date - start_date

        file_set = set()
        for i in range(delta.days+1):
            day = start_date + timedelta(days=i)
            file_set.add(date.strftime(day, '%m-%d-%Y.csv'))

        return file_set

    @staticmethod
    async def _download_file(session, url, download_path):
        """Get a file given a URL, and write it locally in binary mode.

        :param session: OBJ; aiohttp.ClientSession() session
        :param url: STR; file hosting URL
        :param download_path: OBJ; Path object specifying where to save
            the downloaded file
        :return: None
        """

        async with session.get(url) as response:
            if response.status == 200:
                with open(download_path, 'wb') as file:
                    async for data in response.content:
                        file.write(data)

    async def _download_file_list(self):
        files = []
        try:
            r = requests.get(self.index_url, timeout=1)
            html_doc = r.content
            soup = BeautifulSoup(html_doc, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                path = link.attrs.get('href')
                if path[-4:] == '.csv':
                    file_name = path.rsplit('/', 1)[-1]
                    files.append(file_name)
        except (ConnectTimeout, ConnectionError) as e:
            print(e, "\n Unable to fetch updated data.  "
                     "Proceeding with existing data.")
            files = self._create_file_set()

        return files

    async def download_files(self, replace_existing=False):
        """Download new data files from GitHub.

        :param replace_existing: BOOL; if True, overwrite local files
        :return: None
        """

        files_to_download = await self._list_files_to_download(replace_existing)

        async with aiohttp.ClientSession() as session:
            tasks = []
            for file in files_to_download:
                file_path = Path.joinpath(self.raw_data_dir, file)
                download_path = ''.join([self.download_url, file])
                task = asyncio.ensure_future(self._download_file(
                    session, download_path, file_path))
                tasks.append(task)
            await asyncio.gather(*tasks, return_exceptions=True)

    @staticmethod
    async def file_exists(directory, file, extension):
        """Test whether a given file exists.

        Given a file name like "02-14-2020.csv", this function will
        find whether "02-14-2020.png" (or any other combination of the
        file stem with the given extension) exists in the search
        directory.

        :param directory: OBJ; Path object of directory to search
        :param file: OBJ; Path object containing file name to find
        :param extension: STR; file extension to search
        :return: BOOL
        """

        file_stem = file.stem
        image_name = ''.join([file_stem, extension])
        image_path = Path.joinpath(directory, image_name)
        if image_path.is_file():
            return True
        return False

    @staticmethod
    def _get_set_diff(superset, existing_set):
        """Get a list of files present in one set but not another.

        :param superset: SET; typically a set of possible files
            available for download
        :param existing_set: SET; typically a set of files already on
            disk
        :return: LIST; the items in superset not present in existing_set
        """

        try:
            set_diff = superset.difference(existing_set)
        # An AttributeError is thrown if superset doesn't have the
        # difference attribute, and a TypeError is thrown if
        # existing_set is not iterable (such as None in both cases).
        except (AttributeError, TypeError):
            return []
        else:
            diff = list(set_diff)

        return diff

    async def _list_files_to_download(self, replace_existing):
        """Generate a list of files to download.

        If replace_existing is True, download all possible files.
        Otherwise, limit the download list to those not already
        existing locally.

        :param replace_existing: BOOL; if True, overwrite local files
        :return: LIST; file names to download
        """

        possible_files = self._create_file_set()
        if replace_existing is True:
            files_to_download = list(possible_files)
        else:
            files_to_download = self._get_set_diff(
                possible_files, self.local_raw_csvs)

        return files_to_download

    def _find_local_raw_csvs(self):
        """Return a set of files in the form '05-09-2020.csv'."""

        files = set()
        if self.raw_data_dir.is_dir():
            for file in self.raw_data_dir.iterdir():
                files.add(file.name)

        return files
