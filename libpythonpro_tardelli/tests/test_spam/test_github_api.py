from unittest.mock import Mock

import pytest

from libpythonpro_tardelli import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/694103?v=4'
    resp_mock.json.return_value = {
        'login': 'tiagotardelli', 'id': 694103, 'node_id': 'MDQ6VXNlcjY5NDEwMw==',
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonpro_tardelli.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('tiagotardelli')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('tiagotardelli')
    assert 'https://avatars.githubusercontent.com/u/694103?v=4' == url
