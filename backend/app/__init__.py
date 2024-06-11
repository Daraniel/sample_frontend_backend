from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from app.config import load_config
from app.data_source import get_data_source
from app.data_source import get_data_source, BaseDataSource
from app.logger import setup_logger
from app.routes import create_data_blueprint, create_home_blueprint


def create_app(config_file='config/config.yaml'):
    app = Flask(__name__, template_folder='../templates')

    # Load configuration
    config = load_config(config_file)
    app.config.update(config['app'])

    # Set up logger
    setup_logger(app)

    # Initialize data source
    data_source = get_data_source(config)

    # Register the blueprints
    register_blueprints(app, data_source)

    CORS(app)

    return app


def register_blueprints(app, data_source: BaseDataSource):
    api_url = '/api'
    api_spec_url = f'{api_url}/spec'  # Endpoint to serve the API specification
    swagger_url = '/swagger'  # Endpoint to serve the Swagger UI configuration

    # Create and register the data blueprint
    data_bp = create_data_blueprint(data_source)
    app.register_blueprint(data_bp, url_prefix=api_url)
    swagger_ui_blueprint = get_swaggerui_blueprint(
        swagger_url,  # Swagger UI static files will be mapped to {SWAGGER_URL}/
        api_spec_url,
        config={  # Swagger UI config overrides
            'app_name': "Data API"
        }
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix=swagger_url)

    # Create an endpoint to serve the Swagger specification
    @app.route(api_spec_url)
    def swagger_spec():
        from flask_swagger import swagger
        swag = swagger(app)
        swag['info']['title'] = "Data API"
        swag['info']['version'] = "1.0"
        return jsonify(swag)

    # Register and register the home blueprint, should be done at end
    home_bp = create_home_blueprint(api_url=api_spec_url, swagger_url=swagger_url)
    app.register_blueprint(home_bp)
