import requests
import pytest


@pytest.mark.parametrize('url', ['https://google.com', 'https://youtube.com'])
def test_status_code(url):
    """Simple test"""
    request = requests.get(url=url)
    assert request.status_code == 200
