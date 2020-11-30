#!/usr/bin/env python

from datetime import date, timedelta
from pathlib import Path, PosixPath
from unittest.mock import call

import pandas as pd
from pandas import testing
import pytest
from requests.exceptions import ConnectTimeout, ConnectionError

import covid_by_county.data_handler as data_handler
from tests.unit.fixtures import data_handler_data

_MODULE = 'covid_by_county.data_handler'


"""
Upon instantiation, a DataObject runs _validate_file_data(), which not 
only creates a new DataFrame from a CSV file, but runs a number of 
methods on the DataFrame to clean the data.

The sample data (lists of data and lists of column names) in 
data_handler_data.py can be combined to give the DataFrames to be used 
as *input* into the various cleanup methods.

The table below indicates which data list and column list to use as 
input for a particular method to get the expected outcome.

primitive data | primitive cols | input for:
-------------- | -------------- | ------------
raw_data | raw_cols | dropna()
raw_data | lowercased_cols | _remove_non_us_rows()
raw_data | lowercased_cols | _remove_unnecessary_columns()
raw_data | lowercased_cols | _remove_unrecognized_fips()
dropna_data | lowercased_cols | _left_pad_fips()
dropna_data | lowercased_cols | _make_column_names_lowercase()
neccessarycol_data | necessary_cols | _create_log_bins()
neccessarycol_data | necessary_cols | _add_date_column()

Expected outcomes are defined in data_handler_data.py.
"""


def test_add_date_column(data_obj):
    """Test data_handler.DataObject._add_date_column.

    :param data_obj: OBJ; pytest fixture providing an instance of the
        DataObject class
    :return: None
    """
    """Test create_data_dirs when directories already exist."""

    # Arrange
    input_data = data_handler_data.neccessarycol_data
    input_cols = data_handler_data.necessary_cols
    input_df = pd.DataFrame(input_data, columns=input_cols)
    expected = data_handler_data.datecol_df

    # Act
    actual = data_obj._add_date_column(input_df)

    # Assert
    testing.assert_frame_equal(actual, expected)


@pytest.mark.parametrize('col, expected', [
    (0, '0'),
    (1, '1'),
    (10, '2'),
    (11, '2'),
    (100, '3'),
    (101, '3'),
    (1000, '4'),
    (1001, '4'),
    (10000, '5'),
    (10001, '5'),
    (100000, '6'),
    (100001, '6'),
    (1000000, '7'),
    (1000001, '7'),
    (-5, '-1'),
])
def test_assign_bins(col, expected, data_obj):
    """Test data_handler.DataObject._assign_bins.

    :param col: INT; numeric input representing COVID-19 cases or deaths
    :param expected: STR; logarithmic bin
    :param data_obj: OBJ; pytest fixture providing an instance of the
        DataObject class
    :return: None
    """

    # Arrange

    # Act
    actual = data_obj._assign_bins(col)

    # Assert
    assert actual == expected


def test_create_log_bins(data_obj):
    """Test data_handler.DataObject._create_log_bins.

    :param data_obj: OBJ; pytest fixture providing an instance of the
        DataObject class
    :return: None
    """

    # Arrange
    input_data = data_handler_data.neccessarycol_data
    input_cols = data_handler_data.necessary_cols
    input_df = pd.DataFrame(input_data, columns=input_cols)
    expected = data_handler_data.logbins_df

    # Act
    actual = data_obj._create_log_bins(input_df)

    # Assert
    testing.assert_frame_equal(actual, expected)


def test_left_pad_fips(data_obj):
    """Test data_handler.DataObject._left_pad_fips.

    :param data_obj: OBJ; pytest fixture providing an instance of the
        DataObject class
    :return: None
    """

    # Arrange
    input_data = data_handler_data.dropna_data
    input_cols = data_handler_data.lowercased_cols
    input_df = pd.DataFrame(input_data, columns=input_cols)
    expected = data_handler_data.leftpaddedfips_df

    # Act
    actual = data_obj._left_pad_fips(input_df)

    # Assert
    testing.assert_frame_equal(actual, expected)


def test_make_column_names_lowercase(data_obj):
    """Test data_handler.DataObject._make_column_names_lowercase.

    :param data_obj: OBJ; pytest fixture providing an instance of the
        DataObject class
    :return: None
    """

    # Arrange
    input_data = data_handler_data.dropna_data
    input_cols = data_handler_data.lowercased_cols
    input_df = pd.DataFrame(input_data, columns=input_cols)
    expected = data_handler_data.lowercasedcols_df

    # Act
    actual = data_obj._make_column_names_lowercase(input_df)

    # Assert
    testing.assert_frame_equal(actual, expected)


def test_remove_non_us_rows(data_obj):
    """Test data_handler.DataObject._remove_non_us_rows.

    :param data_obj: OBJ; pytest fixture providing an instance of the
        DataObject class
    :return: None
    """

    # Arrange
    input_data = data_handler_data.raw_data
    input_cols = data_handler_data.lowercased_cols
    input_df = pd.DataFrame(input_data, columns=input_cols)
    expected = data_handler_data.us_df

    # Act
    actual = data_obj._remove_non_us_rows(input_df)
    actual.reset_index(inplace=True, drop=True)
    expected.reset_index(inplace=True, drop=True)

    # Assert
    testing.assert_frame_equal(actual, expected)


def test_remove_unnecessary_columns(data_obj):
    """Test data_handler.DataObject._remove_unnecessary_columns.

    :param data_obj: OBJ; pytest fixture providing an instance of the
        DataObject class
    :return: None
    """

    # Arrange
    input_data = data_handler_data.raw_data
    input_cols = data_handler_data.lowercased_cols
    input_df = pd.DataFrame(input_data, columns=input_cols)
    expected = data_handler_data.neccessarycol_df

    # Act
    actual = data_obj._remove_unnecessary_columns(input_df)

    # Assert
    testing.assert_frame_equal(actual, expected)


def test_remove_unrecognized_fips(data_obj):
    """Test data_handler.DataObject._remove_unrecognized_fips.

    :param data_obj: OBJ; pytest fixture providing an instance of the
        DataObject class
    :return: None
    """

    # Arrange
    input_data = data_handler_data.raw_data
    input_cols = data_handler_data.lowercased_cols
    input_df = pd.DataFrame(input_data, columns=input_cols)
    expected = data_handler_data.recognizedfips_df

    # Act
    actual = data_obj._remove_unrecognized_fips(input_df)
    actual.reset_index(inplace=True, drop=True)
    expected.reset_index(inplace=True, drop=True)

    # Assert
    testing.assert_frame_equal(actual, expected)



    # Arrange

    # Act

    # Assert