import pytest

from app import create_app, load_config


@pytest.fixture
def config():
    loaded_config = load_config('test_config.yaml')
    return loaded_config


@pytest.fixture
def app(config):
    app = create_app('test_config.yaml')

    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
