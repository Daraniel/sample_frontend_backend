# data_source Module Documentation

This documentation provides an overview and usage instructions for the data source module which supports retrieving data
from Excel files or SQLite databases. It includes handling different data levels and metadata extraction.

## Overview

The data source module is designed to provide a uniform interface for accessing data from different sources such as
Excel files and SQLite databases. It supports filtering data by different levels and extracting metadata from the data
source.

## Classes and Enums

### `DataLevel` (Enum)

Enumeration to define data levels.

- `LEVEL1 = '1'`
- `LEVEL2 = '2'`
- `LEVEL3 = '3'`

### `BaseDataSource` (ABC)

Abstract base class for data sources, all subsequent data sources must inherit from it.

#### Methods

- `get_data(self, table_name: str, data_level: DataLevel) -> pd.DataFrame`: Abstract method to retrieve data.
- `get_metadata(self, table_name: str) -> pd.DataFrame`: Abstract method to retrieve metadata.

### `FileDataSource` (BaseDataSource)

Abstract base class for file-based data sources.

#### Methods

- `get_data(self, table_name: str, data_level: DataLevel) -> pd.DataFrame`: Abstract method to retrieve data.
- `get_metadata(self, table_name: str) -> pd.DataFrame`: Abstract method to retrieve metadata.

### `ExcelDataSource` (FileDataSource)

Class for data sources based on Excel files.

#### Methods

- `__init__(self, file_name: str)`: Initializes the Excel data source with the specified file name.
- `get_data(self, table_name: str, data_level: DataLevel) -> pd.DataFrame`: Retrieves data from the specified Excel
  sheet and data level.
- `get_metadata(self, table_name: str) -> pd.DataFrame`: Retrieves metadata from the specified Excel sheet.

### `DatabaseDataSource` (BaseDataSource)

Semi-abstract base class for database-based data sources.

#### Methods

- `__init__(self, connection_string)`: Initializes the database data source with the specified connection string.
- `get_data(self, table_name, data_level: DataLevel) -> pd.DataFrame`: Retrieves data from the specified database table
  and data level.
- `get_metadata(self, table_name: str) -> pd.DataFrame`: Abstract method to retrieve metadata.

### `SQLiteDataSource` (DatabaseDataSource)

Class for data sources based on SQLite databases. This data source supports creating a database from an Excel file if
needed. Please note that only '1.1' and '3.1' tables will get auto generated. This decision is made to allow fast
creation of database in this limited project.

#### Methods

- `__init__(self, db_path: str, create_tables_from_excel: bool = False, excel_file: str = None)`: Initializes the SQLite
  data source with the specified database path and optional Excel file for table creation.
- `create_tables_from_excel_file(self)`: Creates database tables from the specified Excel file.
- `create_table_from_sheet(self, sheet_name: str, sheet_data: pd.DataFrame)`: Creates a table in the database from the
  specified sheet data.
- `get_data(self, table_name, data_level: DataLevel) -> pd.DataFrame`: Retrieves data from the specified database table
  and data level.
- `get_metadata(self, table_name: str) -> pd.DataFrame`: Method to retrieve metadata, this method is not implemented as
  definition of metadata in this project is different from the traditional definition and handling it would require
  creating another table containing project metadata which for the sake of simplicity was skipped.

### `get_data_source(config)`

Function to get the appropriate data source based on the configuration.

#### Parameters

- `config` (dict): Configuration dictionary containing the data source type and parameters.

#### Returns

- `BaseDataSource`: An instance of the appropriate data source class.

## Exceptions

### `MetadataNotFoundException` (Exception)

Raised when metadata cannot be found.

### `DataNotFoundException` (Exception)

Raised when data cannot be found.

### `DataSourceException` (Exception)

Raised for general data source-related errors.

## Usage Example

```python
from app.data_source import get_data_source, DataLevel

config = {
    'data_source': {
        'type': 'sqlite',
        'sqlite': {
            'db_path': 'my_database.db',
            'create_tables_from_excel': False,
            'excel_file': 'example.xlsx'
        }
    }
}

data_source = get_data_source(config)
data = data_source.get_data('table_name', DataLevel.LEVEL1)
metadata = data_source.get_metadata('table_name')
```
