# routes Module Documentation

This module sets up Flask blueprints and RESTful API resources for handling data requests. It includes the configuration
for Swagger UI and API documentation, as well as utility functions for registering resources and metadata endpoints.

This file is designed to allow registering APIs for each table (with a similar data structure to the current tables) in
a single line and will dynamically create the end-point and swagger/api documentation for them.

## Classes

### `GenericDataResource`

A generic class for handling data requests, allowing registering new data sources (tables) that match the schema of the
existing tables in one line.

#### `__init__(self, data_source: BaseDataSource, table_name: str, data_description: str)`

Initializes the resource with a data source, table name, and data description.

#### `handle_data_request(get_data_func, table_name, data_level)`

Fetches data for a specific data level.

#### `handle_metadata_request(get_metadata_func, table_name)`

Fetches metadata.

#### `get(self, data_level)`

Handles GET requests to fetch data for a specific level from the table.

#### `get_metadata(self)`

Handles GET requests to fetch metadata from the table.

## Functions

### `add_resource_to_api(api, resource_name, table_name, data_source)`

Helper function to create and add resource and its metadata to the API, allows one-line addition of new tables.

#### Parameters

- **api**: The API object.
- **resource_name**: The name of the resource, used to create the api url.
- **table_name**: The name of the table to get the resources from.
- **data_source**: Data source to get the data from (BaseDataSource object).

#### Usage Example

```python
from flask import Blueprint
from flask_restful import Api
from app.data_source import BaseDataSource
from app.routes import add_resource_to_api


# Create and configure your data source
class MyDataSource(BaseDataSource):
    pass


data_source = MyDataSource()

# Create a blueprint
data_bp = Blueprint('data', __name__)
api = Api(data_bp)

# Add resources in one line to the endpoint
add_resource_to_api(api, resource_name='Bruftoinlandsprodukt_in_jeweiligen_Preisen', table_name='1.1',
                    data_source=data_source)
add_resource_to_api(api, resource_name='Erwerbstaefige', table_name='3.1', data_source=data_source)
```

This will result of creation of the following endpoints where `data_level` is `'1'`, `'2'`, or `'3'`:

##### bruftoinlandsprodukt_in_jeweiligen_preisen

- **Data at wanted level {data_level}**:
  [http://127.0.0.1:5000/api/bruftoinlandsprodukt_in_jeweiligen_preisen/{data_level}](http://127.0.0.1:5000/api/bruftoinlandsprodukt_in_jeweiligen_preisen/{data_level})
- **Metadata**:
  [http://127.0.0.1:5000/api/bruftoinlandsprodukt_in_jeweiligen_preisen/metadata](http://127.0.0.1:5000/api/bruftoinlandsprodukt_in_jeweiligen_preisen/metadata)

##### erwerbstaefige

- **Data at wanted level {data_level}**:
  [http://127.0.0.1:5000/api/erwerbstaefige/{data_level}](http://127.0.0.1:5000/api/erwerbstaefige/{data_level})
- **Metadata**:
  [http://127.0.0.1:5000/api/erwerbstaefige/metadata](http://127.0.0.1:5000/api/erwerbstaefige/metadata)

Please note that the routing to the api may differ depending on your project configuration.

### `create_data_blueprint(data_source)`

Creates a Flask blueprint for the data endpoints (get data at a specific level and get metadata).

#### Parameters

- **data_source**: Data source to get the data from.

#### Returns

- **Blueprint**: The created data blueprint.

### `create_home_blueprint()`

Creates a Flask blueprint for the home page, which contains information about the data blueprint.

#### Parameters

- **api_spec_url**: Url on which api spec is served
- **swagger_url**: Url on which swagger is served

#### Returns

- **Blueprint**: The created home blueprint.

## Usage Example

```python
from flask import Flask
from app.data_source import BaseDataSource
from app.routes import create_data_blueprint, create_home_blueprint

app = Flask(__name__)


# Create and configure your data source
class MyDataSource(BaseDataSource):
    pass


data_source = MyDataSource()

# Register the data blueprint
data_blueprint = create_data_blueprint(data_source)
app.register_blueprint(data_blueprint, url_prefix='/data')

# Register the home blueprint
home_blueprint = create_home_blueprint()
app.register_blueprint(home_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
```
