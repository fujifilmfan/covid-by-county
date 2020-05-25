#!/usr/bin/env python

from os import environ
from pathlib import Path
import re

# Constants in order of typical or expected use in the script.
_SOURCE_DATA_INDEX_URL = ('https://github.com/'
                          'CSSEGISandData/COVID-19/tree/master/'
                          'csse_covid_19_data/csse_covid_19_daily_reports')
_SOURCE_DATA_DOWNLOAD_URL = ('https://raw.githubusercontent.com/'
                             'CSSEGISandData/COVID-19/master/'
                             'csse_covid_19_data/csse_covid_19_daily_reports/')
_PACKAGE_DIR = Path(__file__).absolute().parent.parent
_RAW_DATA_DIR = Path.joinpath(_PACKAGE_DIR, 'raw_data')
_PROCESSED_DATA_DIR = Path.joinpath(_PACKAGE_DIR, 'processed_data')
_REFERENCE_DATA_DIR = Path.joinpath(_PACKAGE_DIR, 'reference_data')
_GEODATA = str(Path.joinpath(_REFERENCE_DATA_DIR, 'geojson-counties-fips.json'))
_PNG_DIR = Path.joinpath(_PACKAGE_DIR, 'png')
_START_DATE = (2020, 1, 22)
_FIGURE_CREATOR = Path.joinpath(
    _PACKAGE_DIR, 'covid_by_county/create_figures.py')


class Config:

    def __init__(self):

        self.package_dir = _PACKAGE_DIR
        self.raw_data_dir = _RAW_DATA_DIR
        self.processed_data_dir = _PROCESSED_DATA_DIR
        self.reference_data_dir = _REFERENCE_DATA_DIR
        self.geodata = _GEODATA
        self.png_dir = _PNG_DIR
        self.source_data_index_url = self._set_source_data_index_url()
        self.source_data_download_url = self._set_source_data_download_url()
        self.start_date = _START_DATE
        self.figure_creator = _FIGURE_CREATOR

        self.version = self._get_version()

    def _get_version(self):
        # The version line in 'pyproject.toml' looks like this:
        # version = "0.20.1"
        pyproject = '/'.join([str(self.package_dir), 'pyproject.toml'])
        pattern = re.compile(
            r"""(version\s=\s")             # 1 beginning
                (\d{1,4}\.\d{1,4}\.\d{1,4}) # 2 the part we want, like "0.20.1"
                ("\n)                       # 3 end
                """, re.VERBOSE)
        match = None

        try:
            with open(pyproject) as f:
                for line in f:
                    if match is not None:
                        break
                    else:
                        match = re.match(pattern, line)
        except FileNotFoundError as e:
            raise e

        try:
            version = match.group(2)
        # An AttributeError is thrown when match is None.
        except AttributeError as e:
            raise e

        return version

    @staticmethod
    def _set_source_data_index_url():
        if ('SOURCE_DATA_INDEX_URL' in environ and
                environ['SOURCE_DATA_INDEX_URL'] != ''):
            source_data_index_url = environ['SOURCE_DATA_INDEX_URL']
        else:
            source_data_index_url = _SOURCE_DATA_INDEX_URL

        return source_data_index_url

    @staticmethod
    def _set_source_data_download_url():
        if ('SOURCE_DATA_DOWNLOAD_URL' in environ and
                environ['SOURCE_DATA_DOWNLOAD_URL'] != ''):
            source_data_download_url = environ['SOURCE_DATA_DOWNLOAD_URL']
        else:
            source_data_download_url = _SOURCE_DATA_DOWNLOAD_URL

        return source_data_download_url


# Instance of Config to be used wherever needed.
configuration = Config()
