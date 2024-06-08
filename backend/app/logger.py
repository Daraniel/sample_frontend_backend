import logging
from logging.handlers import RotatingFileHandler


def setup_logger(app):
    log_level = app.config.get('log_level', 'DEBUG')
    log_format = app.config.get('log_format', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_to_console = app.config.get('log_to_console', True)
    log_to_file = app.config.get('log_to_file', True)
    log_file = app.config.get('log_file', 'app.log')
    log_max_bytes = app.config.get('log_max_bytes', 10000)
    log_backup_count = app.config.get('log_backup_count', 1)

    formatter = logging.Formatter(log_format)

    logger = logging.getLogger()
    logger.setLevel(getattr(logging, log_level.upper()))

    if log_to_file:
        file_handler = RotatingFileHandler(log_file, maxBytes=log_max_bytes, backupCount=log_backup_count)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    app.logger = logger
