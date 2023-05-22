#!/usr/bin/env python3
"""Module cotains class TestGithuborClient 
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
import requests

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Class to test GithubOrg 
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, organization: str, mock: unittest.mock.patch):
        """
       method tests org
        """
        tester_class = GithubOrgClient(organization)
        tester_class.org()
        mock.assert_called_once_with(
            f'https://api.github.com/orgs/{organization}'
        )

    def test_public_repos_url(self):
        """mehtod tests public organization repos """
        with patch.object(
                GithubOrgClient, 'org', new_callable=PropertyMock) as mock:
            mock.return_value = {"repos_url": "test"}
            tester_class = GithubOrgClient('test')
            val = tester_class._public_repos_url
            self.assertEqual(val, mock.return_value['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        method tests public repos
        """
        payload = [{"name": "Google"}, {"name": "Facebook"}]
        mock_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "hello/world"
            tester_class = GithubOrgClient('test')
            val = tester_class.public_repos()

            verify = [
                {"name": i} for i in val
            ]
            self.assertEqual(verify, payload)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ unit-test for GithubOrgClient.has_license """
        res = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(res, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Class for Integration tests"""

    @classmethod
    def setUpClass(cls):
        """Class method that's called before tests are run"""

        conf = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **conf)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """method does Integration test for public repos"""
        tester_class = GithubOrgClient("google")

        self.assertEqual(tester_class.org, self.org_payload)
        self.assertEqual(tester_class.repos_payload, self.repos_payload)
        self.assertEqual(tester_class.public_repos(), self.expected_repos)
        self.assertEqual(tester_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """mehtod does Integration test for public repos with License """
        test_classer = GithubOrgClient("google")

        self.assertEqual(tester_class.public_repos(), self.expected_repos)
        self.assertEqual(tester_class.public_repos("XLICENSE"), [])
        self.assertEqual(tester_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """method called after tests in an individual class are run"""
        cls.get_patcher.stop()
