import config
import file_logging


if __name__ == "__main__":

    config.read_cmd_parameters()
    if not config.production:
        file_logging.log_info("APP Started")
