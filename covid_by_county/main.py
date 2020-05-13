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

import covid_by_county.config as app_config
from covid_by_county.create_figure import create_figure
from covid_by_county.validate_data import validate_data
from covid_by_county.file_handler import FileHandler


config = app_config.configuration


class DataHandler:

    def __init__(self, file):
        """

        :param file: OBJ; PathLib PosixFile object
        """

        self.date = file.stem
        self.file_path = file
        self.validated_data = self._process_file_data()

    def _process_file_data(self):
        raw_dataframe = pd.read_csv(self.file_path)
        raw_dataframe.dropna(inplace=True)
        raw_dataframe['date'] = self.date

        return validate_data(raw_dataframe)

    def _get_figure(self):
        if self.validated_data is not None:
            figure = create_figure(
                self.validated_data, self.date, config.geodata)

            return figure
        return None

    def show_figure(self):
        figure = self._get_figure()
        if figure is not None:
            figure.show()

    def save_figure(self):
        figure = self._get_figure()
        file_name = ''.join([self.date, '.png'])
        image_path = Path.joinpath(config.png_dir, file_name)

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


async def main(args):
    """

    :param args: LIST; like ['-t 40']
    :return: None
    """

    parsed_args = return_parsed_args(args)

    start_time = time.time()

    file_handler = FileHandler(start_date=(2020, 5, 1))
    await file_handler.download_new_files(download_file_list=False)

    dataframes_by_date = {}
    # def create_file_data_objects():
    #     for file in config.raw_data_dir.iterdir():
    #         dataframes_by_date[file.stem] = DataHandler(file)

    duration = time.time() - start_time
    print(f"Downloaded files in {duration} seconds.")
    # create_date_list()

if __name__ == '__main__':
    import sys
    asyncio.run(main(sys.argv[1:]))
