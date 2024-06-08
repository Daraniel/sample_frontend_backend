import pytest


def test_data_endpoint_valid(client):
    response = client.get('/api/bruftoinlandsprodukt_in_jeweiligen_preisen/1')
    assert response.status_code == 200
    assert 'data' in response.json
    assert response.json['status'] == 'success'


def test_data_endpoint_invalid(client):
    response = client.get('/api/bruftoinlandsprodukt_in_jeweiligen_preisen/4')
    assert response.status_code == 400
    assert response.json['status'] == 'error'
    assert response.json['message'] == 'Invalid data level'


def test_metadata_endpoint(client):
    response = client.get('/api/bruftoinlandsprodukt_in_jeweiligen_preisen/metadata')
    assert response.status_code == 200
    assert 'metadata' in response.json
    assert response.json['status'] == 'success'


def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the Data API!' in response.data
    assert b'Available endpoints:' in response.data
    assert b'bruftoinlandsprodukt_in_jeweiligen_preisen' in response.data
    assert b'erwerbstaefige' in response.data


if __name__ == '__main__':
    pytest.main()
