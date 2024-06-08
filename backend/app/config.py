import yaml
from cerberus import Validator

config_schema = {
    'app': {
        'type': 'dict',
        'schema': {
            'secret_key': {'type': 'string', 'default': 'default_secret_key'},
            'debug': {'type': 'boolean', 'default': False},
            'log_file': {'type': 'string', 'default': 'app.log'},
            'log_level': {'type': 'string', 'allowed': ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                          'default': 'INFO'},
            'log_format': {'type': 'string', 'default': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'},
            'log_to_console': {'type': 'boolean', 'default': True},
            'log_to_file': {'type': 'boolean', 'default': True},
            'log_max_bytes': {'type': 'integer', 'min': 100, 'default': 10000},
            'log_backup_count': {'type': 'integer', 'min': 0, 'default': 1},
        }
    },
    'data_source': {
        'type': 'dict',
        'schema': {
            'type': {'type': 'string', 'allowed': ['sqlite', 'excel'], 'default': 'sqlite'},
            'sqlite': {
                'type': 'dict',
                'schema': {
                    'db_path': {'type': 'string', 'default': 'my_database.db'},
                    'create_tables_from_excel': {'type': 'boolean', 'default': False},
                    'excel_file': {'type': 'string', 'default': 'example.xlsx'},
                },
                'required': False
            },
            'excel': {
                'type': 'dict',
                'schema': {
                    'file_name': {'type': 'string', 'default': 'example.xlsx'},
                },
                'required': False
            }
        }
    }
}


def load_config(config_file: str = 'config/config.yaml'):
    """
    Loads, validates, and normalizes the config file

    :param config_file: path to the config file
    :return: the validated config file
    """
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return validate_config(config, config_schema)


def validate_config(config, schema):
    """
    Validates and normalizes the config against the provided schema
    :param config: config to validate
    :param schema: config schema
    :return:
    """
    v = Validator(schema, allow_unknown=True)
    if not v.validate(config):
        raise ValueError(f"Configuration validation error: {v.errors}")
    return v.normalized(config)
