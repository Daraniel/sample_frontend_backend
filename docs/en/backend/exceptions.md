# exceptions Module Documentation

This documentation provides an overview and usage instructions for the custom exceptions used in the application. These
exceptions help in handling and categorizing various errors that may occur within the application, particularly related
to data sources.

## Overview

The exceptions module defines custom exception classes to provide more specific error handling. These exceptions are
structured hierarchically, allowing for catching specific errors as well as broader categories of errors.

## Classes

### `AppException` (Exception)

Base exception class for all application errors.

### `DataSourceException` (AppException)

Base exception class for data source-related errors. Inherits from `AppException`.

### `DataNotFoundException` (DataSourceException)

Raised when data is not found in the specified table. Inherits from `DataSourceException`.

### `MetadataNotFoundException` (DataSourceException)

Raised when metadata is not found in the specified table. Inherits from `DataSourceException`.

## Usage Example

These exceptions can be used to handle specific error cases in the application, particularly when working with data
sources such as databases or files. Here's a sample usage scenario within a data source module:

```python
from app.exceptions import DataNotFoundException, MetadataNotFoundException


def get_data(table_name):
    try:
        # Code to retrieve data from a table
        if not data:
            raise DataNotFoundException(f"No data found for table {table_name}")
    except DataNotFoundException as e:
        print(f"Error: {e}")
        # Handle the error, e.g., return a default value or re-raise the exception


def get_metadata(table_name):
    try:
        # Code to retrieve metadata from a table
        if not metadata:
            raise MetadataNotFoundException(f"No metadata found for table {table_name}")
    except MetadataNotFoundException as e:
        print(f"Error: {e}")
        # Handle the error, e.g., return a default value or re-raise the exception
```
