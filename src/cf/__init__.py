"""Top-level package for cf."""

__author__ = """cf"""
__email__ = "tyz@1token.trade"
__version__ = "0.1.0"
import sys

from loguru import logger as global_logger


logger = global_logger.bind(name="cf")

logger.add(
    sink=sys.stderr,
    format="<green>{time:HH:mm:ss.SSS}</green> | <level>{level:8}</level> | {file.name}:{line} <cyan>{message}</cyan>",
    level="DEBUG",
)


def init():
    init_loguru_global()


def init_loguru_global():

    # 12:56:05.284 | DEBUG    | download_image.py:93

    global_logger.remove()  # 移除默认的 handler

    global_logger.add(
        sink=sys.stderr,
        format="<green>{time:HH:mm:ss.SSS}</green> | <level>{level:8}</level> | {file.name}:{line} <cyan>{message}</cyan>",
        level="DEBUG",
    )
