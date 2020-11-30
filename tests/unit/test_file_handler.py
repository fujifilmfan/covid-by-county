#!/usr/bin/env python

from datetime import date, timedelta
from pathlib import Path, PosixPath
from unittest.mock import call

import pytest
from requests.exceptions import ConnectTimeout, ConnectionError

import covid_by_county.file_handler as file_handler
from tests.unit.fixtures import file_handler_data

_MODULE = 'covid_by_county.file_handler'
# Set the base path to
# /Users/acetone/projects/misc_python/covid_by_county/tests/unit/fixtures/data_dirs/
_PACKAGE_DIR = Path(__file__).absolute().parent
_FIXTURES = Path.joinpath(_PACKAGE_DIR, 'fixtures')
_DATA_DIRS = Path.joinpath(_FIXTURES, 'data_dirs')

RAW_DATA_DIR = Path.joinpath(_DATA_DIRS, 'raw_data')
PROCESSED_DATA_DIR = Path.joinpath(_DATA_DIRS, 'processed_data')
REFERENCE_DATA_DIR = Path.joinpath(_DATA_DIRS, 'reference_data')
PNG_DIR = Path.joinpath(_DATA_DIRS, 'png')


def create_test_dirs():
    dirs_to_create = [
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        REFERENCE_DATA_DIR,
        PNG_DIR,
    ]
    for directory in dirs_to_create:
        if not directory.is_dir():
            directory.mkdir()


def delete_test_dirs():
    """Delete items in data_dirs/ recursively."""
    for directory in _DATA_DIRS.iterdir():
        for item in directory.iterdir():
            if item.is_dir():
                item.rmdir()
            else:
                item.unlink()
        directory.rmdir()


def test_create_data_dirs_if_nonexistent(mock_create_dir):
    """Test create_data_dirs when directories don't already exist."""

    # Arrange
    handler = file_handler.FileHandler(
        raw_data_dir=RAW_DATA_DIR,
        processed_data_dir=PROCESSED_DATA_DIR,
        reference_data_dir=REFERENCE_DATA_DIR,
        png_dir=PNG_DIR
    )
    mock_create_dir(_MODULE)

    expected = [
        call(PosixPath(RAW_DATA_DIR)),
        call(PosixPath(PROCESSED_DATA_DIR)),
        call(PosixPath(REFERENCE_DATA_DIR)),
        call(PosixPath(PNG_DIR)),
    ]

    # Act
    delete_test_dirs()
    handler.create_data_dirs()
    # actual = handler._create_dir.call_args_list

    # Assert
    handler._create_dir.assert_has_calls(expected, any_order=True)


def test_create_data_dirs_if_existent(mock_create_dir):
    """Test create_data_dirs when directories already exist."""

    # Arrange
    handler = file_handler.FileHandler(
        raw_data_dir=RAW_DATA_DIR,
        processed_data_dir=PROCESSED_DATA_DIR,
        reference_data_dir=REFERENCE_DATA_DIR,
        png_dir=PNG_DIR
    )
    mock_create_dir(_MODULE)

    # Act
    delete_test_dirs()
    create_test_dirs()
    handler.create_data_dirs()

    # Assert
    handler._create_dir.assert_not_called()
    delete_test_dirs()


def test_create_file_set():
    """Test _create_file_set."""

    # Arrange
    two_days_ago = date.today() - timedelta(days=2)
    start_date = (two_days_ago.year, two_days_ago.month, two_days_ago.day)
    handler = file_handler.FileHandler(start_date=start_date)

    expected = 3

    # Act
    actual = handler._create_file_set()

    # Assert
    assert len(actual) == expected


@pytest.mark.asyncio
async def test_download_file_list_no_csvs(mock_requests_get):
    """Test _download_file_list in an HTML file with no csv links.

    :param mock_requests_get: OBJ; pytest fixture
    :return: None
    """

    # Arrange
    status = 200
    response = file_handler_data.page_with_zero_csv_links
    mock_requests_get(_MODULE, response, status)
    expected = []
    handler = file_handler.FileHandler()

    # Act
    actual = await handler._download_file_list()

    # Assert
    assert actual == expected


@pytest.mark.asyncio
async def test_download_file_list_four_csvs(mock_requests_get):
    """Test _download_file_list in an HTML file with four csv links.

    :param mock_requests_get: OBJ; pytest fixture
    :return: None
    """

    # Arrange
    status = 200
    response = file_handler_data.page_with_four_csv_links
    mock_requests_get(_MODULE, response, status)
    expected = [
        '03-30-2020.csv',
        '03-31-2020.csv',
        '04-01-2020.csv',
        '04-02-2020.csv',
    ]
    handler = file_handler.FileHandler()

    # Act
    actual = await handler._download_file_list()

    # Assert
    assert actual == expected


@pytest.mark.asyncio
@pytest.mark.parametrize('exception', [ConnectTimeout, ConnectionError])
async def test_download_file_list_exception(
        exception, mock_requests_exception, mock_create_file_set):
    """Test _download_file_list exception handling.

    :param exception: OBJ
    :param mock_requests_exception: OBJ; pytest fixture
    :param mock_create_file_set: OBJ; pytest fixture
    :return: None
    """

    # Arrange
    mock_requests_exception(_MODULE, exception)
    file_set = set()
    mock_create_file_set(_MODULE, file_set)
    handler = file_handler.FileHandler()
    expected = file_set

    # Act
    actual = await handler._download_file_list()

    # Assert
    assert actual == expected


@pytest.mark.asyncio
@pytest.mark.parametrize('file, expected', [
    (Path('test_file_handler'), True),
    (Path('non-existent_file'), False),
])
async def test_file_exists(file, expected):
    """Test file_handler.file_exists.

    :param file: OBJ; Path object of file name to find
    :param expected: BOOL
    :return: None
    """

    # Arrange
    handler = file_handler.FileHandler()

    # Act
    actual = await handler.file_exists(_PACKAGE_DIR, file, '.py')

    # Assert
    assert actual == expected


@pytest.mark.parametrize('superset, existing_set, expected', [
    (set('abc'), set('ac'), ['b']),
    (set('ab'), set('abc'), []),
    (set('abc'), None, []),
    (None, None, []),
])
def test_get_set_diff(superset, existing_set, expected):
    """Test file_handler._get_set_diff.

    :param superset: SET; represents possible files available for
        download
    :param existing_set: SET; represents files already on disk
    :param expected: LIST; items in superset not in existing set
    :return: None
    """

    # Arrange
    handler = file_handler.FileHandler()

    # Act
    actual = handler._get_set_diff(superset, existing_set)

    # Assert
    assert actual == expected


@pytest.mark.asyncio
@pytest.mark.parametrize('possible, bool_, expected', [
    (sorted(set('abc')), True, ['a', 'b', 'c']),
    (sorted(set('abc')), False, ['a', 'b', 'c']),
])
async def test_list_files_to_download(
        possible, bool_, expected, mock_create_file_set, mock_get_set_diff):
    """Test _list_files_to_download.

    :param possible: SET; represents possible files available for
        download
    :param bool_: BOOL; determines whether to replace existing files
    :param expected: LIST; represents items to download
    :param mock_create_file_set: OBJ; pytest fixture
    :param mock_get_set_diff: OBJ; pytest fixture
    :return: None
    """

    # Arrange
    mock_create_file_set(_MODULE, possible)
    mock_get_set_diff(_MODULE, expected)
    handler = file_handler.FileHandler()

    # Act
    actual = await handler._list_files_to_download(bool_)

    # Assert
    assert actual == expected


def test_find_local_raw_csvs():
    """Test file_handler._find_local_raw_csvs."""

    # Arrange
    handler = file_handler.FileHandler(raw_data_dir=RAW_DATA_DIR)

    # Act
    actual = handler._find_local_raw_csvs()
    expected = set()

    # Assert
    assert actual == expected
