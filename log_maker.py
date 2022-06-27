import logging

formatter = logging.Formatter('[%(levelname)s][%(asctime)s] - %(message)s')
def setup_logger(name, log_file, level=logging.INFO):
        """To setup as many loggers as you want"""
        handler = logging.FileHandler(log_file,'a+','utf-8')
        handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger


logger_info = setup_logger('info_logger', '.\script-excel-to-sqlerver\logs\logs.log')
logger_error = setup_logger('error_logger', '.\script-excel-to-sqlerver\logs\error_logs.log')



