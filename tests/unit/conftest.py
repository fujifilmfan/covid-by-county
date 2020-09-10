#!/usr/bin/env python

from asyncio import Future, Task
import pytest


# ================================================
#     Helpers
# ================================================

def return_async_iterator(val):
    class AsyncIt:
        def __init__(self, val):
            self.val = list(val)

        def __aiter__(self):
            return self

        async def __anext__(self):
            if len(self.val) > 0:
                return self.val.pop()
            raise StopAsyncIteration

    return AsyncIt(val)


async def return_async_value(val):
    return val


@pytest.fixture
def mock_generic_object():

    class GenericObject(object):

        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    return GenericObject


@pytest.fixture
def patch_object(mocker):
    """Patch an object with a needed attribute."""

    def _object(obj_to_patch, attribute, return_value):
        mock_func = mocker.patch.object(obj_to_patch, attribute)
        if return_value is not None:
            mock_func.return_value = return_value

    return _object


# ================================================
#     file_handler.py fixtures
# ================================================


# @pytest.fixture(scope='module')
# def mock_asyncio():
#     """Asyncio object for mocking asyncio.Task."""
#
#     class Asyncio(object):
#
#         def __init__(self):
#             pass
#
#         def task(self):
#             pass
#
#     asyncio = Asyncio()
#
#     return asyncio
#
#
# @pytest.fixture
# def mock_asyncio_ensure_future(mocker):
#     """Mock asyncio.ensure_future."""
#
#     def _asyncio_ensure_future(module, return_value):
#         mock_func = mocker.patch(f'{module}.asyncio.ensure_future')
#         mock_func.return_value = return_value
#
#     return _asyncio_ensure_future
#
#
# @pytest.fixture
# def mock_asyncio_gather(mocker):
#     """Mock asyncio.gather."""
#
#     def _asyncio_gather(module):
#        mocker.patch(f'{module}.asyncio.gather')
#
#     return _asyncio_gather


@pytest.fixture
def mock_create_dir(mocker):
    """Mock file_handler.FileHandler._create_dir."""

    def _create_dir(module):
        mocker.patch(f'{module}.FileHandler._create_dir')

    return _create_dir


@pytest.fixture
def mock_create_file_set(mocker):
    """Mock file_handler.FileHandler._create_file_set."""

    def _create_file_set(module, return_value):
        mock_func = mocker.patch(f'{module}.FileHandler._create_file_set')
        # return_val = return_async_value(return_value)
        # mock_func.return_value = set(await return_val)
        mock_func.return_value = return_value

    return _create_file_set


@pytest.fixture
def mock_find_local_raw_csvs(mocker):
    """Mock file_handler.FileHandler._find_local_raw_csvs."""

    def _find_local_raw_csvs(module, return_value):
        mock_func = mocker.patch(f'{module}.FileHandler.find_local_raw_csvs')
        mock_func.return_value = return_value

    return _find_local_raw_csvs


@pytest.fixture
def mock_list_files_to_download(mocker):
    """Mock file_handler._list_files_to_download."""

    def _list_files_to_download(module, return_value):
        mock_func = mocker.patch(
            f'{module}.FileHandler._list_files_to_download')
        mock_func.return_value = return_async_value(return_value)

    return _list_files_to_download


@pytest.fixture
def mock_path(mocker):
    """Mock clip.Path to get a different path than the default."""

    def _path(module, side_effect):
        mock_func = mocker.patch(f'{module}.Path.mkdir')
        mock_func.side_effect = side_effect

    return _path


@pytest.fixture
def mock_path_mkdir(mocker):
    """Mock clip.Path to get a different path than the default."""

    def _path(obj_to_patch, attribute, side_effect):
        mock_func = mocker.patch.object(obj_to_patch, attribute)
        mock_func.side_effect = side_effect

    return _path


@pytest.fixture
def mock_requests_get(mocker, mocked_requests_get):
    """Mock the requests.get return value.

    If we try to set attributes on requests.get directly, we'll
    get "AttributeError: can't set attribute", so we'll mock the
    return value.
    """

    def _requests_get(module, content, status):
        mock_func = mocker.patch(f'{module}.requests.get')
        mock_func.return_value = mocked_requests_get(content, status)

    return _requests_get


@pytest.fixture
def mock_requests_exception(mocker):
    """Simulate requests raising an exception."""

    def _requests_exception(module, exception):
        mock_func = mocker.patch(f'{module}.requests.get')
        mock_func.side_effect = exception

    return _requests_exception


@pytest.fixture
def mocked_requests_get():
    """Create a fake requests.Response object."""

    class MockResponse:
        def __init__(self, _content, _status):
            self.content = _content
            self.status_code = _status

        def content(self):
            return self.content

    return MockResponse

