def test_hello_api(client):
    req = client.get('/hello')
    assert b'Ok' in req.data
