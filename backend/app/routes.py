from flask import Blueprint, url_for, current_app, render_template
from flask_restful import Api, Resource

from app.data_source import DataLevel, DataSourceException, BaseDataSource

class GenericDataResource(Resource):
    def __init__(self, data_source: BaseDataSource, table_name: str, data_description: str):
        self.data_source = data_source
        self.table_name = table_name
        self.data_description = data_description

    @staticmethod
    def handle_data_request(get_data_func, table_name, data_level):
        """Fetch data for a specific level"""
        try:
            level = DataLevel(data_level)
            data = get_data_func(table_name, level)
            return ({'status': 'success',
                     'data': data.drop(columns=['NUTS 1', 'NUTS 2', 'NUTS 3']).to_json(orient='records')},
                    200)
        except ValueError:
            return {'status': 'error', 'message': 'Invalid data level'}, 400
        except DataSourceException as e:
            return {'status': 'error', 'message': str(e)}, 500

    @staticmethod
    def handle_metadata_request(get_metadata_func, table_name):
        """Fetch metadata"""
        try:
            metadata = get_metadata_func(table_name)
            return {'status': 'success', 'metadata': metadata}, 200
        except DataSourceException as e:
            return {'status': 'error', 'message': str(e)}, 500

    def get(self, data_level):
        """
        Fetch data for a specific level from this table
        ---
        parameters:
          - name: data_level
            in: path
            type: string
            required: true
            description: The data level (1, 2, 3)
            default: "1"
        responses:
          200:
            description: Data retrieved successfully
            schema:
              properties:
                status:
                  type: string
                  default: success
                data:
                  type: array
                  items:
                    type: object
                    properties:
                      Lfd. Nr.:
                        type: integer
                        description: 'Lfd. Nr.'
                      EU-Code:
                        type: string
                        description: 'EU-Code'
                      Regional-schlüssel:
                        type: string
                        description: 'Regional-schlüssel'
                      Land:
                        type: string
                        description: 'Land'
                      Gebietseinheit:
                        type: string
                        description: 'Gebietseinheit'
                      '1992':
                        type: number
                        description: '1992'
                        format: float
                      '1994':
                        type: number
                        description: '1994'
                        format: float
                      '1995':
                        type: number
                        description: '1995'
                        format: float
                      '1996':
                        type: number
                        description: '1996'
                        format: float
                      '1997':
                        type: number
                        description: '1997'
                        format: float
                      '1998':
                        type: number
                        description: '1998'
                        format: float
                      '1999':
                        type: number
                        description: '1999'
                        format: float
                      '2000':
                        type: number
                        description: '2000'
                        format: float
                      '2001':
                        type: number
                        description: '2001'
                        format: float
                      '2002':
                        type: number
                        description: '2002'
                        format: float
                      '2003':
                        type: number
                        description: '2003'
                        format: float
                      '2004':
                        type: number
                        description: '2004'
                        format: float
                      '2005':
                        type: number
                        description: '2005'
                        format: float
                      '2006':
                        type: number
                        description: '2006'
                        format: float
                      '2008':
                        type: number
                        description: '2008'
                        format: float
                      '2009':
                        type: number
                        description: '2009'
                        format: float
                      '2010':
                        type: number
                        description: '2010'
                        format: float
                      '2011':
                        type: number
                        description: '2011'
                        format: float
                      '2012':
                        type: number
                        description: '2012'
                        format: float
                      '2013':
                        type: number
                        description: '2013'
                        format: float
                      '2014':
                        type: number
                        description: '2014'
                        format: float
                      '2015':
                        type: number
                        description: '2015'
                        format: float
                      '2016':
                        type: number
                        description: '2016'
                        format: float
                      '2017':
                        type: number
                        description: '2017'
                        format: float
                      '2018':
                        type: number
                        description: '2018'
                        format: float
                      '2019':
                        type: number
                        description: '2019'
                        format: float
                      '2020':
                        type: number
                        description: '2020'
                        format: float
                      '2021':
                        type: number
                        description: '2021'
                        format: float
          400:
            description: Invalid data level
            schema:
              properties:
                status:
                  type: string
                  default: error
                message:
                  type: string
                  default: Invalid data level
          500:
            description: Internal Server Error
            schema:
              properties:
                status:
                  type: string
                  default: error
                message:
                  type: string
                  default: An error occurred
        """
        return GenericDataResource.handle_data_request(self.data_source.get_data, self.table_name, data_level)

    def get_metadata(self):
        """
        Fetch metadata from this table
        ---
        responses:
          200:
            description: Metadata retrieved successfully
            schema:
              properties:
                status:
                  type: string
                  default: success
                metadata:
                  type: string
                  description: Metadata content
          500:
            description: Internal Server Error
            schema:
              properties:
                status:
                  type: string
                  default: error
                message:
                  type: string
                  default: An error occurred
        """
        return GenericDataResource.handle_metadata_request(self.data_source.get_metadata, self.table_name)


def add_resource_to_api(api, resource_name, table_name, data_source):
    """
    Helper function to create and add resource and its metadata to the API.

    :param api: The API object
    :param resource_name: The name of the resource
    :param table_name: The name of the table to get the resources from
    :param data_source: Data source to get the data from
    """
    resource_instance = GenericDataResource(
        data_source, table_name, "Bruftoinlandsprodukt data"
    )

    resource_class = type(resource_name, (Resource,), {'get': resource_instance.get})
    api.add_resource(resource_class, f'/{resource_name.lower()}/<string:data_level>')

    metadata_class = type(f'{resource_name}Metadata', (Resource,), {'get': resource_instance.get_metadata})
    api.add_resource(metadata_class, f'/{resource_name.lower()}/metadata')


def create_data_blueprint(data_source):
    data_bp = Blueprint('data', __name__)
    api = Api(data_bp)

    # Create resource instances for different endpoints and add them to the API
    add_resource_to_api(api, 'Bruftoinlandsprodukt_in_jeweiligen_Preisen', '1.1', data_source)
    add_resource_to_api(api, 'Erwerbstaefige', '3.1', data_source)

    return data_bp


def create_home_blueprint(api_url, swagger_url):
    """
    Dynamically generate the web app blueprint for home page which contains info about the data blueprint

    Please note that this function should only be called after registering all other blueprints.

    :return: Generated blueprint
    """
    home_bp = Blueprint('home', __name__)

    @home_bp.route('/')
    def home():
        """Home route that provides information about the API endpoints."""
        endpoints = {}
        for rule in current_app.url_map.iter_rules():
            if rule.endpoint.startswith('data.'):
                endpoint_name = rule.endpoint.split('.')[-1]
                if endpoint_name.endswith('metadata'):
                    try:
                        # Provide a default value for required parameters
                        url = url_for(rule.endpoint, _external=True)
                    except Exception as e:
                        # If there's an error, it means we need to handle the parameters differently
                        continue

                    base_name = endpoint_name.split('metadata')[0]
                    endpoints.setdefault(base_name, {})['metadata'] = url
                else:
                    try:
                        # Create dictionary for data levels
                        data_levels = {
                            1: url_for(rule.endpoint, data_level='1', _external=True),
                            2: url_for(rule.endpoint, data_level='2', _external=True),
                            3: url_for(rule.endpoint, data_level='3', _external=True)
                        }
                    except Exception as e:
                        # If there's an error, it means we need to handle the parameters differently
                        continue

                    base_name = endpoint_name.split('<')[0].split('/')[-1]
                    endpoints.setdefault(base_name, {})['data'] = data_levels

        api_info = {
            'message': 'Welcome to the Data API!',
            'endpoints': endpoints,
            'swagger_url': url_for('swagger_spec', _external=True).split(api_url)[0] + swagger_url,
            'api_spec': url_for('swagger_spec', _external=True)
        }
        return render_template('home.html', api_info=api_info)

    return home_bp
