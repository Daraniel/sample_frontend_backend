# Flask Backend Setup Documentation

This documentation provides an overview and usage instructions for setting up a Flask backend application with
configuration, logging, data source initialization, and API endpoint registration.

Please refer to the docs folder for indepth details about this project.

## Overview

This Flask backend application is designed to provide RESTful APIs for client applications. It includes functionality to
load configuration settings from a YAML file, set up logging, initialize a data source, and register various API
endpoints and blueprints, including Swagger UI for API documentation.

## Main Dependencies

- `flask`: For creating the web application.
- `flask-restful`: For creating RESTful APIs with Flask.
- `flask_cors`: For enabling Cross-Origin Resource Sharing (CORS) in Flask applications.
- `flask_swagger`: For generating Swagger documentation from the Flask app.
- `flask_swagger_ui`: For serving Swagger UI to document the API.
- `pyyaml`: For loading configuration from YAML files.
- `cerberus`: For validating configuration data.

## Installation

1. Clone the repository: `git clone https://github.com/Daraniel/sample_frontend_backend/`
2. Navigate to the backend directory: `cd backend`
3. Install dependencies: `pip install -r /path/to/requirements.txt`

## Running the App

- Start the server: `python app.py`
- Navigate to the URL provided by the Flask server (default: [http://localhost:5000](http://localhost:5000)) in your
  browser to view the app:

    - A simple homepage containing a list of APIs under `/`.
    - API endpoints will be available under `/api`.
    - API spec will be available under `/api/spec`.
    - Swagger UI will be available under `/swagger`.

## Error Handling

The application includes basic error handling for configuration loading and validation. If the configuration validation
fails, a `ValueError` is raised with details about the validation errors.
