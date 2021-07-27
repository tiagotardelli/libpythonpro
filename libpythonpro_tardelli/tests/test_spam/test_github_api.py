from unittest.mock import Mock

from libpythonpro_tardelli import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'tiagotardelli', 'id': 694103, 'node_id': 'MDQ6VXNlcjY5NDEwMw==',
        'avatar_url': 'https://avatars.githubusercontent.com/u/694103?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('tiagotardelli')
    assert 'https://avatars.githubusercontent.com/u/694103?v=4' == url
