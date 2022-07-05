import logging

log_fmt =' %(asctime)s - [%(levelname)s] - %(message)s'
filemode = 'w'  # 'w' if you want overwrite log messages, by default log messages is appending
log_date_fmt = "%Y-%m-%d %H:%M:%S"


logging.basicConfig(
                    level=logging.DEBUG,
                    format=log_fmt,
                    filemode=filemode,
                    datefmt=log_date_fmt)

logger = logging.getLogger()
