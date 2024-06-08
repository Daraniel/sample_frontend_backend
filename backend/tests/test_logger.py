import logging
import pytest


def test_setup_logger(app):
    logger = app.logger
    assert logger.name == 'root'
    assert logger.level == logging.DEBUG


if __name__ == '__main__':
    pytest.main()
