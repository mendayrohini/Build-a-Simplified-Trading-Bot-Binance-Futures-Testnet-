from loguru import logger
logger.add("logs/trading_bot.log", rotation="1 MB", level="INFO")
