import configparser
from argparse import ArgumentParser
import utils

cfg = configparser.ConfigParser()
cfg.optionxform = str

cfg.read('config.ini')

enable_logging = cfg['Params'].getboolean('enable_logging')
log_files = cfg['Logs'].get('log_files')
log_info = cfg['Logs'].get('info', '$date$-progress.txt').replace('$date$', utils.get_date_as_string())
log_error = cfg['Logs'].get('error', '$date$-error_file.txt').replace('$date$', utils.get_date_as_string())

if enable_logging:
    utils.check_if_dir_exists(log_files)
    utils.check_if_dir_exists(log_info)
    utils.check_if_dir_exists(log_error)

production = cfg['Params'].getboolean('production')
description = cfg['Params'].getboolean('description')


def read_cmd_parameters():
    # Parsing command line
    global description
    parser = ArgumentParser(description=description)

    args = parser.parse_args()
