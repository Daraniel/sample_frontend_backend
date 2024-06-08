# logger Module Documentation

This documentation provides an overview and usage instructions for the `setup_logger` function, which configures logging for a Flask application. The function sets up logging based on the application's configuration settings.

## Overview

The `setup_logger` function initializes the logging configuration for a Flask application. It supports logging to both console and file, with options for log level, format, file size limits, and backup counts.

#### Parameters

- **app**: The Flask application instance.

#### Configuration Options

The function uses the following configuration options from the Flask app's configuration:

- **log_level**: The logging level (default: 'DEBUG'). Possible values include 'DEBUG', 'INFO', 'WARNING', 'ERROR', and 'CRITICAL'.
- **log_format**: The format for log messages (default: '%(asctime)s - %(name)s - %(levelname)s - %(message)s').
- **log_to_console**: Boolean flag to enable/disable logging to the console (default: True).
- **log_to_file**: Boolean flag to enable/disable logging to a file (default: True).
- **log_file**: The file path for the log file (default: 'app.log').
- **log_max_bytes**: The maximum size in bytes for the log file before it is rotated (default: 10,000 bytes).
- **log_backup_count**: The number of backup files to keep when the log file is rotated (default: 1).

Please refer to the documentation of python's logger for more info about these parameters.

#### Example Configuration

```python
from flask import Flask
from app.logger import setup_logger

app = Flask(__name__)

# Update app configuration
app.config.update(
    log_level='INFO',
    log_format='%(asctime)s - %(levelname)s - %(message)s',
    log_to_console=True,
    log_to_file=True,
    log_file='my_app.log',
    log_max_bytes=1048576,  # 1 MB
    log_backup_count=3
)

# Setup the logger
setup_logger(app)
```
