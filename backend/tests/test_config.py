import pytest

from app.config import load_config, validate_config, config_schema  # Replace 'your_module' with the actual module name


def test_load_config():
    config = load_config('../config/config.yaml')
    assert config['app']['secret_key'] == "your_secret_key"
    assert config['app']['debug'] is True
    assert config['app']['log_file'] == "app.log"


@pytest.fixture
def valid_config():
    return {
        'app': {
            'secret_key': 'your_secret_key',
            'debug': True,
            'log_file': 'app.log',
            'log_level': 'DEBUG',
            'log_format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'log_to_console': True,
            'log_to_file': True,
            'log_max_bytes': 10000,
            'log_backup_count': 1,
        },
        'data_source': {
            'type': 'sqlite',
            'sqlite': {
                'db_path': 'example.db',
                'create_tables_from_excel': True,
                'excel_file': 'example.xlsx',
            },
            'excel': {
                'file_name': 'example.xlsx',
            }
        }
    }


@pytest.fixture
def partial_config():
    return {
        'app': {
            'secret_key': 'your_secret_key',
        },
        'data_source': {
            'type': 'sqlite',
            'sqlite': {
                'db_path': 'example.db',
            }
        }
    }


@pytest.fixture
def invalid_config():
    return {
        'app': {
            'secret_key': '',
            'debug': 'yes',  # Invalid type
            'log_file': 'app.log',
            'log_level': 'DEBUG',
            'log_format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'log_to_console': True,
            'log_to_file': True,
            'log_max_bytes': -1,  # Invalid value
            'log_backup_count': 1,
        },
        'data_source': {
            'type': 'unknown',  # Invalid value
            'sqlite': {
                'db_path': 'example.db',
                'create_tables_from_excel': True,
                'excel_file': 'example.xlsx',
            },
            'excel': {
                'file_name': 'example.xlsx',
            }
        }
    }


def test_valid_config(valid_config):
    validated_config = validate_config(valid_config, config_schema)
    assert validated_config['app']['log_file'] == 'app.log'


def test_partial_config(partial_config):
    validated_config = validate_config(partial_config, config_schema)
    assert validated_config['app']['debug'] == False
    assert validated_config['app']['log_level'] == 'INFO'
    assert validated_config['app']['log_to_console'] == True
    assert validated_config['data_source']['sqlite']['create_tables_from_excel'] == False


def test_invalid_config(invalid_config):
    with pytest.raises(ValueError):
        validate_config(invalid_config, config_schema)


if __name__ == '__main__':
    pytest.main()
