import os

from loguru import logger


# 创建日志目录
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = os.path.join(root_dir, 'logs')
log_file = os.path.join(log_dir, 'analysis_{time}.log')

os.makedirs(log_dir, exist_ok=True)


logger.add(log_file, level="DEBUG")