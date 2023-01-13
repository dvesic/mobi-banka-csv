import config
import file_logging
import do_csv


if __name__ == "__main__":

    config.read_cmd_parameters()
    if not config.production:
        file_logging.log_info("APP Started")

    # Read names
    do_csv.read_names()

    # Read and transform transactions
    transactions = do_csv.process_transaction_file()

    if do_csv.lookup_names_dirty:
        do_csv.write_names()

    for line in transactions:
        print(line)
