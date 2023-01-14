import configparser
import argparse
import utils

cfg = configparser.ConfigParser()
cfg.optionxform = str

cfg.read('config.ini', encoding='utf-8')

# Logging section

enable_logging = cfg['Logs'].getboolean('enable_logging')

log_info = cfg['Logs'].get('info', '$date$-progress.txt').replace('$date$', utils.get_date_as_string())
log_error = cfg['Logs'].get('error', '$date$-error_file.txt').replace('$date$', utils.get_date_as_string())

if enable_logging:
    utils.check_if_dir_exists(log_info)
    utils.check_if_dir_exists(log_error)

# Params section

production = cfg['Params'].getboolean('production')
description = cfg['Params'].get('description')

# App specific section

input_file = cfg['App'].get('input_file')
out_file = cfg['App'].get('out_file')

# Construct name of sum file
out_path, out_filename = utils.path_leaf(out_file)

if out_path == '.':
    out_path = ''

out_file_sum = out_path + 'SUM_' + out_filename

default_cat = cfg['App'].get('default_cat')

lookup_names = cfg['App'].get('lookup_names')

excel_columns = cfg['App'].get('excel_columns')
if excel_columns:
    excel_columns = excel_columns.split(",")
else:
    excel_columns = None

excel_bom = cfg['App'].getboolean('excel_bom')


def read_cmd_parameters():
    # Parsing command line
    global description, input_file, out_file, default_cat
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('-i', '--input_file', default=input_file,
                        help=f'Ime ulaznog CSV fajla (eksport sa banke), default je "{input_file}"',
                        required=False)

    parser.add_argument('-o', '--out_file', default=out_file,
                        help=f'Ime rezultujućeg CSV fajla, default je "{out_file}"',
                        required=False)

    parser.add_argument('-c', '--default_cat', default=default_cat,
                        help=f'Naziv podrazumevane kategorije, ako se ne nađe; default je "{default_cat}"',
                        required=False)

    args = parser.parse_args()

    if args.input_file:
        input_file = args.input_file
    if args.out_file:
        out_file = args.out_file
    if args.default_cat:
        default_cat = args.default_cat
