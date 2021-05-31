import logging.config
from os.path import abspath, dirname, join


__all__ = ["configure_logging"]


LOG_CFG_FILE_NAME = "logging.conf"
log_cfg_file_path = join(
    dirname(abspath(__file__)), LOG_CFG_FILE_NAME
)


def configure_logging() -> None:
    logging.config.fileConfig(
        log_cfg_file_path, disable_existing_loggers=False
    )
