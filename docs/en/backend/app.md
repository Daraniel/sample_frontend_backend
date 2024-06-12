# Flask Application Setup Documentation

This documentation provides an overview and usage instructions for setting up a Flask application with configuration,
logging, data source initialization, and API endpoint registration.

## Overview

This Flask application is designed to load configuration settings from a YAML file, set up logging, initialize a data
source, and register various API endpoints and blueprints, including Swagger UI for API documentation.

## Main Dependencies

- `flask`: For creating the web application.
- `flask-restful`: For creating RESTful APIs with Flask.
- `flask_cors`: For enabling Cross-Origin Resource Sharing (CORS) in Flask applications.
- `flask_swagger`: For generating Swagger documentation from the Flask app.
- `flask_swagger_ui`: For serving Swagger UI to document the API.
- `pyyaml`: For loading configuration from YAML files.
- `cerberus`: For validating configuration data.

## Application Structure

- `config`: Directory containing the configuration files.
- `app`: Package containing the application's source code, including:
    - `__init__.py`: Main module, allows creation of app.
    - `config.py`: Module for loading and validating configuration.
    - `data_source.py`: Module for initializing the data source.
    - `exceptions.py`: Module containing custom exceptions.
    - `logger.py`: Module for setting up logging.
    - `routes.py`: Module for creating and registering API and home blueprints.
- `templates`: Directory containing the template files.
- `tests`: Directory containing tests.

## Main Functions

### `create_app(config_file='config/config.yaml')`

This function creates and configures the Flask application.

#### Parameters

- `config_file` (str): Path to the configuration file. Default is `'config/config.yaml'`.

Please refer to [config documentation](config.md) for more info about how this configuration file.

#### Returns

- `app` (Flask): The configured Flask application.

#### Example

```python
from app import create_app

app = create_app('path/to/config.yaml')
```

### `register_blueprints(app, data_source)`

This function registers the blueprints for the API endpoints and Swagger UI with the Flask application.

#### Parameters

- `app` (Flask): The Flask application.
- `data_source` (BaseDataSource): The data source for the application.

#### Example

```python
from flask import Flask

from app import register_blueprints
from app.config import load_config
from app.data_source import get_data_source

config = load_config('config_file')

app = Flask(__name__)
data_source = get_data_source(config)

register_blueprints(app, data_source)
```

## Usage Example

1. Install the necessary dependencies:

    ```sh
    pip install -r /path/to/requirements.txt
    ```

2. Create or configure the configuration file `config/config.yaml` with the necessary settings.

3. Create the Flask application instance:

    ```python
    from app import create_app
    
    app = create_app('config/config.yaml')
    
    if __name__ == '__main__':
        app.run()
    ```

4. Access the API and Swagger UI:

    - A simple homepage containing a list of apis under `/`.
    - API endpoints will be available under `/api`.
    - API spec will be available under `/api/spec`.
    - Swagger UI will be available under `/swagger`.

Alternatively, the server can be started with the `flask` command which allows direct specification of host and port
with `--host` and `--port` flags.

## Error Handling

The application includes basic error handling for configuration loading and validation. If the configuration validation
fails, a `ValueError` is raised with details about the validation errors.
