import logging
from logging import handlers

class Logging(object):
    def __init__(self, log_name, level):
        self.logger = logging.getLogger(log_name)
        format = logging.Formatter("""
        %(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)
        """)
        self.logger.setLevel(level)
        tfh = handlers.TimedRotatingFileHandler(filename=log_name,
                                                when="D",
                                                backupCount=2,
                                                encoding='utf-8')
        tfh.setFormatter(format)
        self.logger.addHandler(tfh)
