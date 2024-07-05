#!/usr/bin/env python3
"""
Module for testing GithubOrgClient functionality.

This module contains unit and integration tests for verifying the
behavior of the GithubOrgClient class, which interacts with the
GitHub API to retrieve organization and repository data.
"""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for the GithubOrgClient class methods.

    These tests utilize mocking to isolate and verify the behavior
    of individual methods within the GithubOrgClient class.
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """
        Test the org method of GithubOrgClient.

        Verifies that the org method correctly constructs the URL
        and makes a GET request to fetch organization details from
        the GitHub API.
        """
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self):
        """
        Test the _public_repos_url property of GithubOrgClient.

        Mocks the org property to simulate a response containing
        a repository URL and verifies that the _public_repos_url
        property correctly retrieves and returns this URL.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test the public_repos method of GithubOrgClient.

        Mocks the _public_repos_url property and the get_json function
        to simulate fetching a list of repositories from the GitHub API.
        Verifies that the public_repos method correctly processes and
        returns the list of repository names.
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            expected_names = [repo["name"] for repo in json_payload]
            self.assertEqual(result, expected_names)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test the has_license static method of GithubOrgClient.

        Verifies that the has_license method correctly determines
        whether a given repository has a specific license key.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient using fixture data.

    These tests simulate interactions with the GitHub API by
    mocking HTTP responses. They validate that the GithubOrgClient
    class correctly retrieves and processes organization and
    repository data.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up mock responses for HTTP requests.

        Configures mock responses for the requests.get function
        to return predefined JSON payloads based on fixture data.
        """
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """
        Integration test for fetching public repositories.

        Verifies that the GithubOrgClient correctly retrieves
        organization and repository data, and matches expected
        results from fixture data.
        """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """
        Integration test for fetching public repositories with a license.

        Validates that the GithubOrgClient correctly filters and
        returns repositories based on a specified license key,
        in addition to verifying against fixture data.
        """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """
        Clean up after running integration tests.

        Stops the patcher used for mocking HTTP requests once all
        integration tests have completed.
        """
        cls.get_patcher.stop()
