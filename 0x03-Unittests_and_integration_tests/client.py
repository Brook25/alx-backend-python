#!/usr/bin/env python3
"""Module contains a github org. client
"""
from typing import (
    List,
    Dict,
)

from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class GithubOrgClient:
    """Class Github org. Clent
    """
    original_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """init method to initialize an instance of GithubOrgClient"""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """method memoizes org."""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """mehtod returns public repos URL"""
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """method to memoize repos payload"""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """mehtod retuns public repos"""
        json_pload = self.repos_payload
        public_rep = [
            repo["name"] for repo in json_pload
            if license is None or self.has_license(repo, license)
        ]

        return public_rep

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """method validates license"""
        assert license_key is not None, "license_key cannot be None"
        try:
            check_license = access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
        return check_license
