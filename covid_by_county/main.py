#!/usr/bin/env python

import argparse
import asyncio
from datetime import date, datetime, timedelta
import json
import multiprocessing
import os
import psutil
from psutil import NoSuchProcess
import signal
from pathlib import Path
import time

import aiohttp
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import _plotly_utils.colors.sequential
import plotly.express as px
import plotly.io.orca
import plotly.graph_objects as go
import plotly.figure_factory as ff
import requests
from requests.exceptions import ConnectTimeout, ConnectionError
import wget

import covid_by_county.config as app_config
from covid_by_county.data_handler import DataObject
from covid_by_county.create_figures import save_figures, show_figures
from covid_by_county.file_handler import FileHandler


config = app_config.configuration
orca_config = plotly.io.orca.config
# orca_config.timeout = 20


def return_parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(description='')

    return parser.parse_args(args)


async def main(args):
    """

    :param args: LIST; like ['-t 40']
    :return: None
    """
    parsed_args = return_parsed_args(args)

    file_handler = FileHandler(start_date=(2020, 3, 27))
    await file_handler.download_new_files(replace_existing=False)

    start_time = time.time()
    data_array = [(DataObject(file), file_handler.png_dir) for file in
                  file_handler.raw_data_paths]
    pool_pids = []
    all_procs = []
    try:
        with multiprocessing.Pool() as pool:
            pool.starmap(save_figures, data_array)

            all_procs = create_process_list(pool)
            # print(all_procs)

            # pool.close()
            # pool.terminate()
            # pool.join()
            # time.sleep(21)

    except ValueError as e:
        print(e)
        all_procs = create_process_list(pool)
    finally:
        # print('smile')
        # all_procs = create_process_list(pool)
        print(all_procs)
        kill_procs(all_procs)

    # SYNCHRONOUS:
    # data_array = [DataObject(file) for file in file_handler.raw_data_paths]
    # for datum in data_array:
    #     save_figures(datum, file_handler.png_dir)
    duration = time.time() - start_time
    print(f"Images written in {duration} seconds.")
    # time.sleep(20)


def create_process_list(pool):
    pids = []
    proc_list = []
    for fork in pool._pool:
        assert fork.pid != os.getpid()
        pids.append(fork.pid)
    for pid in pids:
        try:
            parent = psutil.Process(pid)
            children = parent.children(recursive=True)
            proc_list.append(parent)
            proc_list.extend(children)
        except NoSuchProcess:
            continue
    return proc_list


def kill_procs(proc_list, sig=signal.SIGTERM, timeout=1):
    for proc in proc_list:
        try:
            proc.send_signal(sig)
            # psutil.wait_procs(proc, timeout=timeout)
        except NoSuchProcess:
            continue


if __name__ == '__main__':
    import sys
    asyncio.run(main(sys.argv[1:]))
