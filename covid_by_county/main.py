#!/usr/bin/env python

import argparse
import asyncio
from datetime import date, datetime, timedelta
import json
from pathlib import Path
import time

import aiohttp
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import _plotly_utils.colors.sequential
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import requests
from requests.exceptions import ConnectTimeout, ConnectionError
import wget

import covid_by_county.config as config
from covid_by_county.create_figure import create_figure
from covid_by_county.validate_data import validate_data


class FileManager:

    def __init__(
            self,
            raw_data_dir=config.configuration.raw_data_dir,
            processed_data_dir=config.configuration.processed_data_dir,
            reference_data_dir=config.configuration.reference_data_dir,
            png_dir=config.configuration.png_dir):
        self.raw_data_dir = raw_data_dir
        self.processed_data_dir = processed_data_dir
        self.reference_data_dir = reference_data_dir
        self.png_dir = png_dir
        self.create_dirs()
        self.local_raw_csvs = self.list_local_raw_csvs()
        self.index_url = config.configuration.source_data_index_url
        self.download_url = config.configuration.source_data_download_url
        self.start_date = config.configuration.start_date

    def create_dirs(self):
        """Create default data and image directories."""

        if not self.raw_data_dir.is_dir():
            self.raw_data_dir.mkdir()
        if not self.processed_data_dir.is_dir():
            self.processed_data_dir.mkdir()
        if not self.reference_data_dir.is_dir():
            self.reference_data_dir.mkdir()
        if not self.png_dir.is_dir():
            self.png_dir.mkdir()

    def list_local_raw_csvs(self):
        """Return a list of files in the form '05-09-2020.csv'."""

        files = []
        for file in self.raw_data_dir.iterdir():
            files.append(file.name)

        return files

    async def download_file(self, session, url, download_path):
        async with session.get(url) as response:
            if response.status == 200:
                with open(download_path, 'wb') as file:
                    async for data in response.content:
                        file.write(data)

    def download_new_files(self, presume=False):
        if presume:
            available_files = set(self.create_file_list())
        else:
            available_files = set(self.files_to_download())
        files_to_download = list(available_files.difference(self.local_raw_csvs))
        async with aiohttp.ClientSession() as session:
            tasks = []
            for file in files_to_download:
                file_path = Path.joinpath(self.raw_data_dir, file)
                if not file_path.is_file():
                    download_path = ''.join([self.download_url, file])
                    task = asyncio.ensure_future(self.download_file(
                        session, download_path, file_path))
                    tasks.append(task)
            await asyncio.gather(*tasks, return_exceptions=True)

    def files_to_download(self):
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

        return files

    def create_file_list(self):
        year, month, day = self.start_date
        start_date = date(year, month, day)
        end_date = date.today()
        delta = end_date - start_date

        file_list = []
        for i in range(delta.days+1):
            day = start_date + timedelta(days=i)
            file_list.append(date.strftime(day, '%m-%d-%Y.csv'))

        return file_list


dataframes_by_date = {}


def create_file_data_objects():
    for file in config.configuration.raw_data_dir.iterdir():
        dataframes_by_date[file.stem] = FileData(file)


class FileData:

    def __init__(self, file):
        """

        :param file: OBJ; PathLib PosixFile object
        """

        self.date = file.stem
        self.file_path = file
        self.validated_data = self.process_file_data()

    def process_file_data(self):
        raw_dataframe = pd.read_csv(self.file_path)
        raw_dataframe.dropna()
        raw_dataframe['date'] = self.date

        return validate_data(raw_dataframe)

    def get_figure(self):
        if self.validated_data is not None:
            figure = create_figure(
                self.validated_data, self.date, config.configuration.geodata)

            return figure
        return None

    def show_figure(self):
        figure = self.get_figure()
        if figure is not None:
            figure.show()

    def save_figure(self):
        figure = self.get_figure()
        file_name = ''.join([self.date, '.png'])
        image_path = Path.joinpath(config.configuration.png_dir, file_name)

        if figure is not None and not image_path.is_file():
            # img_bytes = fig.to_image(format='png')
            figure.write_image(str(image_path))


def return_parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(description='')

    # parser.add_argument('-d', '--download', type=str,
    #                     help="""Download available CSV files.""")
    # parser.add_argument('-s', '--schedule', type=str, help="""Schedule
    #                     slack_munki to post to Slack at the same time
    #                     every day.  Enter the time in HH:MM format.""")
    # parser.add_argument('-t', '--threshold', type=int, help="""Use
    #                     this argument to override the default percent
    #                     utilization value of 80(%%).  Set it to 0 to
    #                     see all results.  This works with slack_munki.py
    #                      whether the --schedule argument is used.""")

    return parser.parse_args(args)


def main(args):
    """

    :param args: LIST; like ['-t 40']
    :return: None
    """

    parsed_args = return_parsed_args(args)

    start_time = time.time()
    # asyncio.get_event_loop().run_until_complete(download_all_files(
    #     config.configuration.source_data_index_url,
    #     config.configuration.source_data_download_url,
    #     config.configuration.raw_data_dir))
    my_manager = FileManager()
    my_manager.create_file_list()
    duration = time.time() - start_time
    print(f"Downloaded files in {duration} seconds.")
    # create_date_list()

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
