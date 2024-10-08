from path import Path
from loguru import logger as _logger

BASE_PATH = Path(__file__).parent.parent
LOGS_PATH = BASE_PATH / 'logs'

log_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS zz}</green> | <b>{message}</b>"
_logger.add(f"{LOGS_PATH}/file.log", format=log_format, colorize=False, backtrace=True, diagnose=True)


def logger(message: str):
    _logger.info(message)
