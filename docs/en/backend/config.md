# config Module Documentation

This documentation provides an overview and usage instructions for the `config` module, which is designed to load and
validate application configuration using YAML and Cerberus.

## Overview

The `config` module is responsible for loading configuration files written in YAML and validating them against a
predefined schema using the Cerberus library. This module ensures that configuration settings meet the expected
structure and value constraints before being used by the application.

## Schema Definition

The configuration schema is defined in the `config_schema` dictionary. The schema covers two main sections: `app`
and `data_source`.

### `app` Schema

- `secret_key`: String, default: `'default_secret_key'`
- `debug`: Boolean, default: `False`
- `log_file`: String, default: `'app.log'`
- `log_level`: String, allowed values: `['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']`, default: `'INFO'`
- `log_format`: String, default: `'%(asctime)s - %(name)s - %(levelname)s - %(message)s'`
- `log_to_console`: Boolean, default: `True`
- `log_to_file`: Boolean, default: `True`
- `log_max_bytes`: Integer, minimum: `100`, default: `10000`
- `log_backup_count`: Integer, minimum: `0`, default: `1`

### `data_source` Schema

- `type`: String, allowed values: `['sqlite', 'excel']`, default: `'sqlite'`
- `sqlite`: Dictionary (Optional)
    - `db_path`: String, default: `'my_database.db'`
    - `create_tables_from_excel`: Boolean, default: `False`
    - `excel_file`: String, default: `'example.xlsx'`
- `excel`: Dictionary (Optional)
    - `file_name`: String, default: `'example.xlsx'`

Please note that `secret_key` here is only defined for the sake of completion and has no direct usage in this project.

### Sample Config File

```yaml
app:
  secret_key: "your_secret_key"
  debug: true
  log_file: "app.log"
  log_level: "DEBUG"  # Can be DEBUG, INFO, WARNING, ERROR, CRITICAL
  log_format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  log_to_console: true
  log_to_file: true
  log_max_bytes: 10000  # Maximum log file size in bytes before rotation
  log_backup_count: 1  # Number of backup files to keep

data_source:
  type: "excel"  # Can be "sqlite" or "excel"
  sqlite:
    db_path: "my_database.db"
    create_tables_from_excel: true  # Flag to create tables from Excel if database is not found
    excel_file: "../vgrdl_r2b1_bs2022_0.xlsx"
  excel:
    file_name: "../vgrdl_r2b1_bs2022_0.xlsx"
```

## Functions

### `load_config(config_file='config/config.yaml')`

This function loads the configuration file specified by the `config_file` parameter.

This function internally uses `validate_config` to validate and normalize the config.

#### Parameters

- `config_file` (str): Path to the configuration file. Default is `'config/config.yaml'`.

#### Returns

- `config` (dict): The loaded configuration as a dictionary.

### `validate_config(config, schema)`

This function validates the loaded configuration against the provided schema.

#### Parameters

- `config` (dict): The configuration dictionary to validate.
- `schema` (dict): The schema to validate against.

#### Returns

- `normalized_config` (dict): The normalized configuration dictionary.

#### Raises

- `ValueError`: If the configuration does not match the schema.

## Usage Example

```python
from app.config import load_config, validate_config

config_schema = {
    # Define your schema here...
}

if __name__ == '__main__':
    config = load_config('file_name')
    validated_config = validate_config(config, config_schema)
    print(validated_config)
```

## Error Handling

If the configuration validation fails, a `ValueError` is raised with details about the validation errors.
