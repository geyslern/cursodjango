from django.test import Client


def test_status_code(client: Client):
    resp = client.get(path='/')
    assert 200 == resp.status_code
