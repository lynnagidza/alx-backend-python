#!/usr/bin/env python3
"""Unittests for utils.py"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from urllib.error import HTTPError
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized


# task 4
class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient Class"""

    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: MagicMock):
        """Test GithubOrgClient.org"""
        github_client = GithubOrgClient(org_name)
        github_client.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')
# end of task 4

# task 5
    def test_public_repos_url(self):
        """Test GithubOrgClient._public_repos_url"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = TEST_PAYLOAD
            github_client = GithubOrgClient('test')
            self.assertEqual(github_client._public_repos_url,
                             mock_public_repos_url.return_value)
            mock_public_repos_url.assert_called_once()
# end of task 5

# task 6
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock):
        """Test GithubOrgClient.public_repos"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = TEST_PAYLOAD
            github_client = GithubOrgClient('test')
            self.assertEqual(github_client.public_repos(),
                             mock_get_json.return_value)
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                mock_public_repos_url.return_value)
# end of task 6

# task 7
    @parameterized.expand(
        [
            ({'license': {'key': 'my_license'}}, 'my_license', True),
            ({'license': {'key': 'other_license'}}, 'my_license', False),
        ]
    )
    def test_has_license(self, repo: dict, license_key: str, expected: bool):
        """Test GithubOrgClient.has_license"""
        github_client = GithubOrgClient('test')
        self.assertEqual(github_client.has_license(repo, license_key),
                         expected)
# end of task 7


# task 8
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient Class"""

    @classmethod
    def setUpClass(cls):
        """setUpClass"""
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """tearDownClass"""
        cls.get_patcher.stop()
# end of task 8

# task 9
    def test_public_repos(self):
        """Test GithubOrgClient.public_repos"""
        github_client = GithubOrgClient('test')
        self.assertEqual(github_client.public_repos(), [])

    def test_public_repos_with_license(self):
        """Test GithubOrgClient.public_repos with license"""
        github_client = GithubOrgClient('test')
        self.assertEqual(github_client.public_repos('test'), [])
# end of task 9
