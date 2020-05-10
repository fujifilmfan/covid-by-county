#!/usr/bin/env python

import argparse
import asyncio
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


PACKAGE_DIR = Path(__file__).absolute().parent
DOWNLOADS_DIR = Path.joinpath(PACKAGE_DIR, 'source_data_downloads')
DATA_INDEX_URL = ('https://github.com/CSSEGISandData/COVID-19/tree/master/'
                  'csse_covid_19_data/csse_covid_19_daily_reports')
DATA_DOWNLOAD_URL = ('https://raw.githubusercontent.com/CSSEGISandData/'
                     'COVID-19/master/csse_covid_19_data/'
                     'csse_covid_19_daily_reports/')
IMAGES_DIR = Path.joinpath(PACKAGE_DIR, 'png')
REFERENCES_DIR = Path.joinpath(PACKAGE_DIR, 'reference_files')
GEODATA = str(Path.joinpath(REFERENCES_DIR, 'geojson-counties-fips.json'))


async def download_file(session, url, download_path):
    async with session.get(url) as response:
        if response.status == 200:
            with open(download_path, 'wb') as file:
                async for data in response.content:
                    file.write(data)


async def download_all_files(data_index_url, data_download_url, dest):
    files = files_to_download(data_index_url)
    if not dest.is_dir():
        dest.mkdir()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for file in files:
            file_path = Path.joinpath(dest, file)
            if not file_path.is_file():
                download_path = ''.join([data_download_url, file])
                task = asyncio.ensure_future(download_file(
                    session, download_path, file_path))
                tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


def files_to_download(data_index_url):
    """

    :param data_index_url:
    :return:
    """
    files = []
    try:
        r = requests.get(data_index_url, timeout=1)
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


class DataProcessor:

    def __init__(self, file):
        """

        :param file: OBJ; PathLib PosixFile object
        """
        self.file = file
        self.file_name = self.file.name
        self.df = None

    def process_file(self):
        self.df = self.read_file_into_df(self.file)
        validate_data(self.df)
        plot_figure(self.df, self.file_name)

    def read_file_into_df(self, file):
        """
        # put in FileHandler, probably
        :param file:
        :return:
        """
        # if file_name in DOWNLOADS_DIR.iterdir():
        # for file in DOWNLOADS_DIR.iterdir():
        #     if file.name == file_name.name:
        raw_df = pd.read_csv(file)
        new_col_names = [column.lower() for column in raw_df.columns]
        raw_df.columns = new_col_names
        raw_df['date'] = file.stem
        return raw_df

    def validate_data(df):
        """
        # do this automatically on import
        :param df:
        :return:
        """
        columns = df.columns
        if 'fips' in columns:
            remove_non_us_rows(df)
            remove_unnecessary_columns(df)
            remove_unrecognized_fips(df)
            df.dropna(inplace=True)
            left_pad_fips(df)
            create_log_bins(df)
            return df

    def remove_non_us_rows(df):
        indices = df[df['country_region'] != 'US'].index
        df.drop(indices, inplace=True)
        return df

    def remove_unrecognized_fips(df):
        """
        Unrecognized FIPS:
        60000: American Samoa
        66000: Guam
        69000: Northern Mariana Islands
        72000: Puerto Rico
        78000: Virgin Islands
        88888: Diamond Princess
        99999: Grand Princess
        """
        unrecognized_fips = [60000, 88888, 99999, 66000, 69000, 78000]
        for fips in unrecognized_fips:
            indices = df[df['fips'] == fips].index
            df.drop(indices, inplace=True)
        return df

    def remove_unnecessary_columns(df):
        columns_to_keep = ['fips', 'confirmed', 'deaths', 'date']
        for column in df.columns:
            if column not in columns_to_keep:
                df.drop(column, axis=1, inplace=True)
        return df

    def left_pad_fips(df):
        # Convert from float64 to int64:
        df['fips'] = df['fips'].astype(int)
        # Convert from int64 to string:
        df['fips'] = df['fips'].astype(str)
        # Add zeros to make fips 5 characters long:
        df['fips'] = df['fips'].str.zfill(5)
        return df

    def create_log_bins(df):
        df['confirmed_bins'] = df['confirmed'].apply(assign_bins)
        df['deaths_bins'] = df['deaths'].apply(assign_bins)
        return df

    def assign_bins(col):
        if col == 0:
            return '0'
        elif 0 < col < 10:
            return '1'
        elif 10 <= col < 100:
            return '2'
        elif 100 <= col < 1000:
            return '3'
        elif 1000 <= col < 10000:
            return '4'
        elif 10000 <= col < 100000:
            return '5'
        elif 100000 <= col < 1000000:
            return '6'
        elif col >= 1000000:
            return '7'


def plot_figure(df, file_name):

# colorscale_r = colorscale[::-1]
    with open(str(Path.joinpath(REFERENCES_DIR, 'geojson-counties-fips.json'))) as f:
        counties = json.load(f)

    # endpoints = list(np.logspace(0.0, 5.0, num=6, base=10.0))

    # The following endpoints map to bins 0, 1, 2, 3, 4, 5, 6, 7.
    endpoints = [0, 1, 10, 100, 1000, 10000, 100000, 1000000]
    fips = df['fips']  #.tolist()
    values = df['confirmed_bins']  #.tolist()
    df['text'] = df['confirmed']

    fig = go.Figure(
        data=go.Choropleth(
            autocolorscale=False,
            colorbar=dict(
                len=0.90,
                tickfont_color='#000000',
                ticktext=endpoints,
                tickvals=list(range(len(endpoints))),
                title='Number of cases',
                title_font_color='#000000',
            ),
            colorscale='Blues',
            geojson=counties,
            hovertext=df['text'],
            locationmode='geojson-id',
            locations=fips,
            marker=dict(
                line_color='black',
                line_width=0.5,
            ),
            showscale=True,
            z=values,
            zmax=7,
            zmin=0,
        )
    )

    fig.update_layout(
        annotations=[
            dict(
                x=1.14,
                yanchor='bottom',
                y=0.96,
                text=file_name[:-4],
                font=dict(
                    color='black',
                    size=16,
                ),
                showarrow=False,
            ),
        ],
        geo=dict(
            resolution=50,
            scope='usa',
        ),
        height=550,
        margin=dict(
            l=10,
            r=10,
            t=10,
            b=10,
        ),
        title=dict(
            font_color='#000000',
            text='Confirmed COVID-19 cases in the United States by county',
            xref='paper',
            y=0.97,
            yanchor='bottom',
            yref='paper',
        ),
        width=1050,
    )
    fig.layout.template = None
    file_name = ''.join([file_name[:-4], '.png'])
    # fig.show()
    # img_bytes = fig.to_image(format='png')
    fig.write_image(str(Path.joinpath(IMAGES_DIR, file_name)))


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

    # if parsed_args.threshold and parsed_args.threshold >= 0:
    #     global utilization_threshold
    #     utilization_threshold = parsed_args.threshold
    # else:
    #     utilization_threshold = 80
    #
    # if parsed_args.schedule:
    #     schedule_slack_munki(parsed_args.schedule)
    # else:
    #     munki_data = get_munki_data()
    #     if parsed_args.post:
    #         post_to_slack(munki_data)
    #     pp.pprint(munki_data)

    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_files(
        DATA_INDEX_URL, DATA_DOWNLOAD_URL, DOWNLOADS_DIR))  # 2, 4, 4, 5, 12,
    # 40 s async  3, 4, 5, 11 s aiofiles
    # download_files(DATA_INDEX_URL, DATA_DOWNLOAD_URL, DOWNLOADS_DIR)
    duration = time.time() - start_time
    print(f"Downloaded files in {duration} seconds.")  # 23, 25, 26, 34,
    # 35 s sync
    for file in DOWNLOADS_DIR.iterdir():
        process_file(file)
    # dataframe = read_file_into_df('04-30-2020.csv')
    # validate_data(dataframe)
    # plot_figure(dataframe)


if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
