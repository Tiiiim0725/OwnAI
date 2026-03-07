"""
日志配置使用示例
logger.info("这是一条info日志")
logger.error("这是一条error日志")
logger.debug("这是一条debug日志")
logger.warning("这是一条warning日志")
"""

import sys
from pathlib import Path

from loguru import logger

# 获取项目根目录（src/logger的上级目录）
PROJECT_ROOT = Path(__file__).parent.parent.parent
LOGS_DIR = PROJECT_ROOT / "logs"

# 确保logs目录存在
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# 移除默认的handler
logger.remove()

# 添加控制台输出（带颜色）
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
    colorize=True
)

# 添加文件输出（按天分割，文件名格式：YYYYMMDD.log）
logger.add(
    LOGS_DIR / "{time:YYYYMMDD}.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG",
    rotation="00:00",  # 每天午夜创建新文件
    retention="30 days",  # 保留30天的日志
    compression="zip",  # 压缩旧日志
    encoding="utf-8"
)

__all__ = ["logger"]
