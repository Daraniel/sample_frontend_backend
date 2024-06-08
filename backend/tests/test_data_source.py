import os
import tempfile
import time

import pytest

from app.data_source import get_data_source, DataLevel


def test_excel_data_source(config):
    config['data_source']['type'] = 'excel'
    excel_source = get_data_source(config)
    data = excel_source.get_data('1.1', DataLevel.LEVEL2)
    assert data is not None
    assert 'NUTS 1' in data
    assert 'NUTS 2' in data
    assert 'NUTS 3' in data

    # make sure data is accessible as intended
    data.drop(columns=['NUTS 1', 'NUTS 2', 'NUTS 3']).to_json(orient='records')

    metadata = excel_source.get_metadata('1.1')
    assert metadata is not None
    assert metadata == '1   Bruttoinlandsprodukt in jeweiligen Preisen 1.1   Bruttoinlandsprodukt in Mill. EUR'


@pytest.fixture
def setup_sqlite_db(config):
    config['data_source']['type'] = 'sqlite'

    # Create a temporary file for the SQLite database
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        db_path = tmp.name

    config['data_source']['sqlite']['db_path'] = db_path
    config['data_source']['sqlite']['create_tables_from_excel'] = True
    try:
        # Ensure the database is removed before running the test
        if os.path.exists(db_path):
            os.remove(db_path)

        yield
    finally:
        # Clean up the temporary database file after the test
        if os.path.exists(db_path):
            delete_file_with_retry(db_path)


def delete_file_with_retry(file_path, max_retries=5, delay=0.1):
    # we might need sometime before the file is ready to be closed (i.e. released by sqlite)
    for _ in range(max_retries):
        try:
            os.remove(file_path)
            return True
        except Exception as e:
            print(f"Failed to delete file: {e}")
            time.sleep(delay)
    return False


def test_sqlite_data_source_creation(config, setup_sqlite_db):
    if config['data_source']['type'] == 'sqlite':
        sqlite_source = get_data_source(config)
        data = sqlite_source.get_data('1.1', DataLevel.LEVEL1)
        assert data is not None

        # make sure data is accessible as intended
        data.drop(columns=['NUTS 1', 'NUTS 2', 'NUTS 3']).to_json(orient='records')

        # getting meta data is not implemented
        # metadata = sqlite_source.get_metadata('1.1', DataLevel.LEVEL1)
        # assert metadata is not None


if __name__ == '__main__':
    pytest.main()
