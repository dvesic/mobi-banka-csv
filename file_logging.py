import config
import logging

logger = None


def get_logger(info_file, error_file):

    logger_instance = logging.getLogger('mobi')
    logger_instance.setLevel(logging.DEBUG)
    logger_instance.addHandler(logging.StreamHandler())

    info_fh = logging.FileHandler(info_file)
    info_fh.setLevel(logging.INFO)

    err_fh = logging.FileHandler(error_file)
    err_fh.setLevel(logging.ERROR)

    # noinspection SpellCheckingInspection
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    info_fh.setFormatter(formatter)
    err_fh.setFormatter(formatter)

    # add the handlers to logger
    logger_instance.addHandler(info_fh)
    logger_instance.addHandler(err_fh)

    return logger_instance


def log_info(message):
    if not config.enable_logging:
        return
    logger.info(message)


def log_error(message):
    if not config.enable_logging:
        return
    logger.error(message)


if config.enable_logging:
    logger = get_logger(config.log_info, config.log_error)
