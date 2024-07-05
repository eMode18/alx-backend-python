#!/usr/bin/env python3
"""
Module for unit testing the utils module functions: access_nested_map,
get_json, and memoize.
"""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the access_nested_map function in the utils module.

    Tests include verifying the function's ability to access nested
    dictionary values using specified paths and raising exceptions
    appropriately when paths do not exist.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """
        Test the access_nested_map function.

        Verifies that the function correctly accesses nested dictionary
        values based on provided paths and returns the expected output.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """
        Test access_nested_map function's exception handling.

        Ensures that access_nested_map raises the expected exceptions
        when attempting to access paths that do not exist within the
        provided nested dictionary.
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Unit tests for the get_json function in the utils module.

    Tests include verifying the function's ability to retrieve JSON
    data from specified URLs using mocked HTTP responses.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """
        Test the get_json function.

        Verifies that the get_json function retrieves JSON data
        from the specified URL and returns the expected payload,
        utilizing mocked responses for HTTP GET requests.
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the memoize decorator function in the utils module.

    Tests include verifying that the memoization mechanism correctly
    caches the results of a method call and returns the cached result
    on subsequent calls.
    """

    def test_memoize(self) -> None:
        """
        Test the memoize decorator function.

        Verifies that the memoize decorator caches the result of a method
        call and returns the cached result on subsequent calls, reducing
        the number of times the method is invoked.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
