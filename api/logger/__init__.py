from os.path import abspath, dirname, join


__all__ = ["LOG_CFG_FILE_PATH"]


LOG_CFG_FILE_NAME = "logging.conf"
LOG_CFG_FILE_PATH = join(
    dirname(abspath(__file__)), LOG_CFG_FILE_NAME
)
