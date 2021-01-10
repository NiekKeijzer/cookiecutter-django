""" Basic tests to ensure views contain the expected response """

from django.test.client import Client


def test_home_view(client: Client) -> None:
    """ Ensure the app has a homepage """
    response = client.get("/")
    assert response.status_code == 200
