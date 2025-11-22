"""Top-level package for cf."""

__author__ = """cf"""
__email__ = "tyz@1token.trade"
__version__ = "0.1.0"
import hashlib
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

from loguru import logger as global_logger


def sanitize_args(args: list[str]) -> str:
    """
    把参数列表转成干净的字符串，作为文件名安全的一部分
    """
    if not args:
        return "default"

    raw = "_".join(args)
    # 替换非法字符为 _
    cleaned = re.sub(r"[^a-zA-Z0-9_\-]", "_", raw)

    # 可选：截断 + 添加 hash 保证唯一性但不长
    if len(cleaned) > 50:
        hash_suffix = hashlib.md5(raw.encode()).hexdigest()[:6]
        cleaned = cleaned[:40] + "_" + hash_suffix

    return cleaned


def sanitize_file_name(file_name: str) -> str:
    """
    把文件名转成干净的字符串，作为文件名安全的一部分
    """
    return re.sub(r"[^a-zA-Z0-9_\-]", "_", file_name)


def get_log_path():
    # 获取入口脚本名，比如 download_image.py
    entry_file = sanitize_file_name(Path(sys.argv[0]).name)

    # 获取传入参数，拼接为 &arg1_arg2
    args = sanitize_args(sys.argv[1:])

    # 拼出日志文件路径
    log_file_name = f"{entry_file}_{args}.jsonl"
    log_file_name = log_file_name.lower()
    log_path = Path.home() / "qblog" / log_file_name
    log_path.parent.mkdir(parents=True, exist_ok=True)
    return log_path


def json_serialize(record):
    payload = {
        "time": record["time"].timestamp(),
        "time_human": record["time"].strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
        "level": record["level"].name,
        "message": record["message"],
        "file": f"{record['file'].name}:{record['line']}",
    }
    return json.dumps(payload)


def formatter(record):
    # Note this function returns the string to be formatted, not the actual message to be logged
    record["extra"]["serialized"] = json_serialize(record)
    return "{extra[serialized]}\n"


logger = global_logger.bind(name="cf")

# 日志格式: INFO [13:30:28.370][file.py:86] message
_LOG_FORMAT = (
    "<level>{level:5}</level> "
    "<dim>[{time:HH:mm:ss.SSS}][{file.name}:{line}]</dim> "
    "<level>{message}</level>"
)

logger.remove()
logger.level("DEBUG", color="<dim>")
logger.level("WARNING", color="<red>")
logger.add(sink=sys.stdout, format=_LOG_FORMAT, level="DEBUG")


@lru_cache(maxsize=1)
def logger_add_path():
    logger.add(
        get_log_path(),
        level="DEBUG",
        rotation="10 MB",
        retention="7 days",
        # serialize=True,
        format=formatter,
    )


def set_log_level(level: str):
    logger.remove()
    logger.add(sink=sys.stdout, format=_LOG_FORMAT, level=level)


def init():
    init_pandas()


def init_pandas():
    import pandas  # noqa: F401

    # TODO set pandas default options
    # pandas.set_option("")
