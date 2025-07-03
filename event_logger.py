import logging
import os
from logging.handlers import TimedRotatingFileHandler

# Ensure logs/ directory exists
os.makedirs("logs", exist_ok=True)

# Create main logger object
logger = logging.getLogger("plc_logger")
logger.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

# Create rotating file handler (1 log file per day)
file_handler = TimedRotatingFileHandler(
    filename="logs/plc_logger.log",
    when="midnight",
    interval=1,
    backupCount=7,
    encoding="utf-8"
)
file_handler.setFormatter(formatter)

# Create console handler (optional: shows in terminal)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Add both handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)