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

    file_handler = FileHandler(start_date=(2020, 3, 27))
    await file_handler.download_new_files(replace_existing=False)

    # data_obj_by_date = {}
    # for file in file_handler.raw_data_paths:
    #     data_obj_by_date[file.stem] = {'data_obj': DataObject(file)}

    # data_objs = []
    # for file in file_handler.raw_data_paths:
    #     data_objs.append(DataObject(file))

    start_time = time.time()
    data_array = [(DataObject(file), file_handler.png_dir) for file in
                  file_handler.raw_data_paths]
    pool_pids = []
    procs = []
    try:
        with multiprocessing.Pool() as pool:
            pool.starmap(save_figures, data_array)

            # pool_pids = []
            for fork in pool._pool:
                pool_pids.append(fork.pid)
            try:
                for pid in pool_pids:
                    parent = psutil.Process(pid)
                    children = parent.children(recursive=True)
                    procs.extend(children)
                for proc in procs:
                    pool_pids.append(proc.pid)
            except NoSuchProcess:
                pass
            print(pool_pids)

            # pool.close()
            # pool.terminate()
            # pool.join()
            # for pid in pool_pids:
            #     kill_proc_tree(pid)
                # print(pid)
                # os.kill(pid, 9)
            # time.sleep(21)
    except ValueError as e:
        print(e)
    finally:
        # print('smile')
        for pid in pool_pids:
            kill_proc_tree(pid)
    # SYNCHRONOUS:
    # data_array = [DataObject(file) for file in file_handler.raw_data_paths]
    # for datum in data_array:
    #     save_figures(datum, file_handler.png_dir)
    duration = time.time() - start_time
    print(f"Images written in {duration} seconds.")
    # time.sleep(20)


def kill_proc_tree(pid, sig=signal.SIGTERM, include_parent=True,
                   timeout=1, on_terminate=None):
    """Kill a process tree (including grandchildren) with signal
    "sig" and return a (gone, still_alive) tuple.
    "on_terminate", if specified, is a callabck function which is
    called as soon as a child terminates.
    """
    assert pid != os.getpid(), "won't kill myself"
    try:
        parent = psutil.Process(pid)
        children = parent.children(recursive=True)
        if include_parent:
            children.append(parent)
        for p in children:
            p.send_signal(sig)
        psutil.wait_procs(children, timeout=timeout)
    except NoSuchProcess:
        pass


if __name__ == '__main__':
    import sys
    asyncio.run(main(sys.argv[1:]))
