from datetime import datetime
import os
from pathlib import Path


def file_exists(file_name):
    target_file = Path(file_name)
    return target_file.is_file()


def check_os_access(file_name, right=os.W_OK, to_abort=True):
    result = True
    if not os.access(file_name, os.W_OK):
        print(f"ERROR: Unable to access file [{file_name}] - {right} - ABORTING")
        result = False
        if to_abort:
            quit(1022)

    return result


def check_if_dir_exists(path_or_file, to_abort=True):
    result = True

    file_path = os.path.abspath(path_or_file)
    if not ((path_or_file[-1] == os.sep) or (path_or_file[-1] == '/')):
        left_side = file_path[0:file_path.rindex(os.sep) + len(os.sep)]
        file_name = file_path[file_path.rindex(os.sep) + len(os.sep):]

        if file_name:
            # this is file and not a directory
            file_path = left_side

    if not os.path.exists(file_path):
        print(f"ERROR: Could not locate folder for file [{file_path}] - ABORTING")
        result = False
        if to_abort:
            quit(1023)

    return result


def get_date_as_string(date_arg=None, fmt='%Y%m%d'):
    if date_arg is None:
        date_arg = datetime.today()

    return date_arg.strftime(fmt)


def get_date_as_string_full(date_arg=None):
    return get_date_as_string(date_arg, fmt='%Y%m%d-%H%M%S')


def to_int(number):
    try:
        result = int(number)
    except ValueError:
        result = None
    return result
