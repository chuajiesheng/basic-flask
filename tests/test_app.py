def test_health_check_api(client):
    req = client.get('/health')
    assert b'Ok' in req.data
