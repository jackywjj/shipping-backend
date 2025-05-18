import logging
import sys

import colorlog

from settings import LOG_PATH


def get_logger(level=logging.DEBUG):
    # 创建logger对象
    logger = logging.getLogger()
    logger.setLevel(level)
    handler = logging.StreamHandler(sys.stdout)

    # 创建控制台日志处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # 设置日志格式
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    file_handler = logging.FileHandler(LOG_PATH)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)

    # 定义颜色输出格式
    color_formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:\t%(asctime)s - %(message)s',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )
    # 将颜色输出格式添加到控制台日志处理器
    console_handler.setFormatter(color_formatter)
    # 移除默认的handler
    for handler in logger.handlers:
        logger.removeHandler(handler)
    logger.addHandler(handler)
    logger.addHandler(file_handler)
    # 将控制台日志处理器添加到logger对象
    logger.addHandler(console_handler)
    return logger


logger = get_logger(logging.DEBUG)
