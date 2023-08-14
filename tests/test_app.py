from freezegun import freeze_time


def test_health_check_api(client):
    req = client.get('/health')
    assert b'Ok' in req.data


@freeze_time("2012-01-14 03:21:34", tz_offset=-4)
def test_now_check_api(client):
    req = client.get('/now')
    assert b'2012-01-13T23:21:34+00:00' in req.data
