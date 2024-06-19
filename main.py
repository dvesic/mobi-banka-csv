"""
Set of routines for processing CSV export of transactions from https://online.mobibanka.rs

Details are in README.md, in Serbian, given target audience.
"""

__version__ = '0.27'
__author__ = 'Dejan Vesić, Dejan@Vesic.Org'

import config
import do_csv


if __name__ == "__main__":

    config.read_cmd_parameters()

    # Read names
    do_csv.read_names()

    # Read and transform transactions
    transactions = do_csv.process_transaction_file()

    if do_csv.lookup_names_dirty:
        do_csv.write_names()

    if not config.production:
        for line in transactions:
            print(line)
