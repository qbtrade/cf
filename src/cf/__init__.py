"""Top-level package for cf."""

__author__ = """cf"""
__email__ = "tyz@1token.trade"
__version__ = "0.1.0"
import sys


def init_loguru():
    from loguru import logger

    # 12:56:05.284 | DEBUG    | download_image.py:93

    logger.remove()  # 移除默认的 handler

    logger.add(
        sink=sys.stderr,
        format="<green>{time:HH:mm:ss.SSS}</green> | <level>{level:8}</level> | {file.name}:{line} <cyan>{message}</cyan>",
        level="DEBUG",
    )
