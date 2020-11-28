#!/usr/bin/env python

import argparse
import asyncio
from functools import partial
import multiprocessing
import os
import psutil
from psutil import NoSuchProcess
import signal
import subprocess
import time

from covid_by_county.create_figures import save_figures, show_figures
from covid_by_county.file_handler import FileHandler


def return_parsed_args(args):
    """Parse and define command line arguments.

    :param args: LIST; like ['-t 40']
    :return: OBJ; Namespace object looking something like this:
        Namespace(post=False, schedule=None, threshold=40)
    """

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-d', '--download_new', type=bool, default=True,
                        help="""Download CSV files that exist in the upstream 
                        repository but not in the local data directory. When 
                        False, no files will be downloaded.
                        See also '--replace_existing'.
                        """)
    parser.add_argument('-p', '--process_handling', type=str, default='auto',
                        help="""Options: 'auto' (default) or 'manual'.
                        Since Plotly does not reliably kill Orca processes
                        spawned when multiprocessing is used, the 'auto' 
                        option utilizes the OS to take care of it.
                        The 'manual' option, in which the application keeps 
                        track of the processes and kills them when finished, 
                        runs about twice as fast as the 'auto' option but is 
                        considered higher risk (due simply to my own 
                        inexperience managing process pools manually).
                        """)
    parser.add_argument('--processors', type=int, default=8, help="""Set the 
                        number of processors to use for image creation.
                        """)
    parser.add_argument('-r', '--replace_existing', type=bool, default=False,
                        help="""When False, only files that don't exist 
                        locally will be downloaded from the upstream repo and 
                        written to the local data directory. When True, all 
                        local files will be overwritten with all available 
                        files from the upstream repo.
                        See also '--download_new'.
                        """)
    parser.add_argument('-s', '--start_date', type=str, help="""
                        Use this flag to only download data files that are more 
                        recent than the start date (inclusive).
                        Formats: yyyy-m-d, like '2020-3-27'.  You can also use 
                        leading zeros for the month and day if you prefer.
                        """)
    return parser.parse_args(args)


def intermediate_func(png_dir, figure_creator, data_file):

    subprocess.call(['python', figure_creator, png_dir, data_file])


async def main(args):
    """

    :param args: LIST; like ['-p manual']
    :return: None
    """
    cli_args = return_parsed_args(args)
    download_new = cli_args.download_new
    num_processors = cli_args.processors
    replace_existing = cli_args.replace_existing

    start_date = None
    if cli_args.start_date:
        year, month, day = cli_args.start_date.split('-')
        try:
            year = int(year)
            month = int(month)
            day = int(day)
        except (UnboundLocalError, ValueError) as e:
            print(e, "Year, month, and day must by hyphen-separated integers.")
        else:
            start_date = (year, month, day)

    if start_date:
        file_handler = FileHandler(start_date=start_date)
    else:
        file_handler = FileHandler()
    file_handler.create_data_dirs()

    if download_new is True:
        await file_handler.download_files(replace_existing=replace_existing)

    start_time = time.time()

    data_files = [
        str(file) for file in file_handler.raw_data_paths
        if not await file_handler.file_exists(file_handler.png_dir, file,
                                              '.png')
    ]

    if cli_args.process_handling.lower() == 'auto':
        try:
            with multiprocessing.Pool(num_processors) as pool:
                f = partial(
                    intermediate_func,
                    str(file_handler.png_dir),
                    str(file_handler.figure_creator))

                pool.map(f, data_files)
                pool.close()  # I'm done with the pool
                pool.join()  # Don't move on till it's finished

        except ValueError as e:
            print(e)

    elif cli_args.process_handling.lower() == 'manual':
        all_procs = []
        try:
            with multiprocessing.Pool(num_processors) as pool:
                f = partial(
                    save_figures,
                    str(file_handler.png_dir)
                )
                pool.map(f, data_files)

                all_procs = create_process_list(pool)

        except ValueError as e:
            print(e)
            all_procs = create_process_list(pool)
        finally:
            kill_procs(all_procs)

    else:
        print(f"You entered {cli_args.process_handling} for the '-p' option. "
              f"Allowable options are 'auto' and 'manual' (case insensitive).")

    duration = time.time() - start_time
    print(f"Images written in {duration} seconds.")


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
