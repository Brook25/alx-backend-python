#!/usr/bin/env python3
"""
module with classes for nested map function testing
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Class has unittest methods for nested map function """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """ method for unittesting the function """
        self.assertEqual(access_nested_map(nested_map, path), expected_value)

    @parameterized.expand([
        ({}, ('a',), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b'))
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_value):
        """mehtod for Unittesting for exception in a nested map func """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map=nested_map, path=path)

        self.assertEqual(repr(error.exception), repr(expected_value))


class TestGetJson(unittest.TestCase):
    """method for testing utils.get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Tests utils.get_json with a mock object
        """
        patch_r = patch("utils.requests.get")
        mck_get = patch_r.start()
        mck_get.return_value.ok = payload.get("payload")
        mck_get.return_value.json.return_value = payload
        response = get_json(url)
        self.assertEqual(respnse, payload)
        mock_get.stop()


class TestMemoize(unittest.TestCase):
    """mehtod to test for utils.memoize decorator
    """
    def test_memoize(self):
        """method to test for utils.memoize decorator by mocking a_method
        """
        class TestClass:
            """Class for testing
            """
            def a_method(self):
                """returns a_method"""
                return 42

            @memoize
            def a_property(self):
                """returns a_property"""
                return self.a_method()
        with patch.object(TestClass, "a_method") as mck_a:
            mck_a.return_value = True
            tester = TestClass()
            tester.a_property
            tester.a_property
            mck_a.assert_called_once()


if __name__ == '__main__':
    unittest.main()
