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
        self._create_dirs()
        self.local_raw_csvs = self._list_local_raw_csvs()
        self.index_url = config.source_data_index_url
        self.download_url = config.source_data_download_url
        self.figure_creator = config.figure_creator

    def _create_dirs(self):
        """Create default data and image directories."""

        if not self.raw_data_dir.is_dir():
            self.raw_data_dir.mkdir()
        if not self.processed_data_dir.is_dir():
            self.processed_data_dir.mkdir()
        if not self.reference_data_dir.is_dir():
            self.reference_data_dir.mkdir()
        if not self.png_dir.is_dir():
            self.png_dir.mkdir()

    async def _create_file_list(self):
        year, month, day = self.start_date
        start_date = date(year, month, day)
        end_date = date.today()
        delta = end_date - start_date

        file_list = []
        for i in range(delta.days+1):
            day = start_date + timedelta(days=i)
            file_list.append(date.strftime(day, '%m-%d-%Y.csv'))

        return file_list

    @staticmethod
    async def _download_file(session, url, download_path):
        async with session.get(url) as response:
            if response.status == 200:
                with open(download_path, 'wb') as file:
                    async for data in response.content:
                        file.write(data)

    async def download_new_files(
            self, download_file_list=False, replace_existing=False):
        """

        :param download_file_list:
        :param replace_existing:
        :return:
        """
        # TODO: This function doesn't respect start_date (except in that it
        #  calls _create_file_list()).  Consider using start_date here and
        #  breaking out replace_existing functionality into a new function.
        available_files = set()
        files_to_download = []

        if replace_existing is True:
            files_to_download = await self._create_file_list()
        elif download_file_list is True:
            available_files = set(await self._files_to_download())
        else:
            available_files = set(await self._create_file_list())

        if available_files:
            new_files = available_files.difference(self.local_raw_csvs)
            files_to_download = list(new_files)

        async with aiohttp.ClientSession() as session:
            tasks = []
            for file in files_to_download:
                file_path = Path.joinpath(self.raw_data_dir, file)
                download_path = ''.join([self.download_url, file])
                task = asyncio.ensure_future(self._download_file(
                    session, download_path, file_path))
                tasks.append(task)
            await asyncio.gather(*tasks, return_exceptions=True)

    def file_exists(self, file, extension):
        file_stem = file.stem
        image_name = ''.join([file_stem, extension])
        image_path = Path.joinpath(self.png_dir, image_name)
        if image_path.is_file():
            return True
        return False

    async def _files_to_download(self):
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
            files = await self._create_file_list()

        return files

    def _list_local_raw_csvs(self):
        """Return a list of files in the form '05-09-2020.csv'."""

        files = []
        for file in self.raw_data_dir.iterdir():
            files.append(file.name)

        return files
