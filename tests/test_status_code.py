import requests
import pytest

urls = ['https://google.com', 'https://youtube.com']

@pytest.mark.parametrize('url', urls)
def test_status_code(url):
    """Simple test"""
    request = requests.get(url=url)
    assert request.status_code == 200
