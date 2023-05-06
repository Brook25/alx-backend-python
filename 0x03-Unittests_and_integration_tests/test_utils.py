#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ unittests for nested map function """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_value):
        """ unittest for the function """
        self.assertEqual(access_nested_map(nested_map, path), expected_value)

    @parameterized.expand([
        ({}, ('a',), KeyError('a')),
        ({"a": 1}, ("a", "b"), KeyError('b'))
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_value):
        """ Unittest for exception in a nested map function """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map=nested_map, path=path)

        self.assertEqual(repr(error.exception), repr(expected_value))


class TestGetJson(unittest.TestCase):
    """Testing for utils.get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Tests utils.get_json with a mock object
        """
        patcher = patch("utils.requests.get")
        mock_get = patcher.start()
        mock_get.return_value.ok = payload.get("payload")
        mock_get.return_value.json.return_value = payload
        res = get_json(url)
        self.assertEqual(res, payload)
        mock_get.stop()


class TestMemoize(unittest.TestCase):
    """Testing for utils.memoize decorator
    """
    def test_memoize(self):
        """Testing for utils.memoize decorator by mocking a_method
        """
        class TestClass:
            """A class for testing
            """
            def a_method(self):
                """a_method"""
                return 42

            @memoize
            def a_property(self):
                """a_property"""
                return self.a_method()
        with patch.object(TestClass, "a_method") as mock_a:
            mock_a.return_value = True
            test = TestClass()
            test.a_property
            test.a_property
            mock_a.assert_called_once()


if __name__ == '__main__':
    unittest.main()
