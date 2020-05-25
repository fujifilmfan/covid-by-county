#!/usr/bin/env python

import argparse
import asyncio
from functools import partial
import multiprocessing
import multiprocessing.dummy
import os
from pathlib import Path
import psutil
from psutil import NoSuchProcess
import signal
import subprocess
import time

import plotly.io.orca

import covid_by_county.config as app_config
from covid_by_county.data_handler import DataObject
from covid_by_county.create_figures import save_figures, show_figures
from covid_by_county.file_handler import FileHandler


# config = app_config.configuration
# orca_config = plotly.io.orca.config
# orca_config.timeout = 20


def return_parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(description='')

    return parser.parse_args(args)


def intermediate_func(png_dir, figure_creator, data_file):
    # args = [figure_creator, png_dir, data_file]
    print('working on' + str(data_file))
    subprocess.call(['python', figure_creator, png_dir, data_file])
    # subprocess.check_output(args)


async def main(args):
    """

    :param args: LIST; like ['-t 40']
    :return: None
    """
    parsed_args = return_parsed_args(args)

    file_handler = FileHandler(start_date=(2020, 3, 27))
    await file_handler.download_new_files(replace_existing=False)

    start_time = time.time()
    # data_array = [(DataObject(file), file_handler.png_dir) for file in
    #               file_handler.raw_data_paths]
    # data_files = [str(file) for file in file_handler.raw_data_paths]
    data_files = [
        str(file) for file in file_handler.raw_data_paths if not
        file_handler.file_exists(file, '.png')]
    pool_pids = []
    all_procs = []

    # date = data_obj.date
    # dataframe = data_obj.validated_data
    # file_name = ''.join([date, '.png'])
    # image_path = Path.joinpath(png_dir_path, file_name)

    # for data in data_array:
    # use subprocess to launch a single invocation of the actual worker
    # script with the arguments

    try:
        with multiprocessing.Pool(8) as pool:
            f = partial(
                intermediate_func,
                str(file_handler.png_dir),
                str(file_handler.figure_creator))

            print('Before pool.map()')
            pool.map(f, data_files)
            print('After pool.map() and before pool.close()')

            pool.close()  # I'm done with the pool
            print('After pool.close() and before pool.join()')
            pool.join()  # Don't move on till it's finished
            print('After pool.join()')
            # time.sleep(21)

    except ValueError as e:
        print(e)
    finally:
        pass

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
