#!/usr/bin/env python3
"""Unittests for utils.py"""
import unittest
from unittest.mock import patch, MagicMock
from typing import (
    Mapping,
    Sequence,
    Any
)
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized

# task 0
class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap Class"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
# end of task 0

# task 1
    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ):
        """Test access_nested_map function"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
            self.assertEqual(expected, err.exception)
# end of task 1

# task 2
class TestGetJson(unittest.TestCase):
    """TestGetJson Class"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url: str, test_payload: dict):
        """Test get_json function"""
        mock = MagicMock()
        mock.json.return_value = test_payload
        with patch("requests.get", return_value=mock):
            self.assertEqual(get_json(test_url), test_payload)
# end of task 2

# task 3
class TestMemoize(unittest.TestCase):
    """TestMemoize Class"""

    def test_memoize(self):
        """Test memoize function"""
        class TestClass:
            """TestClass Class"""

            def a_method(self):
                """a_method function"""
                return 42

            @memoize
            def a_property(self):
                """a_property function"""
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock:
            test = TestClass()
            test.a_property
            test.a_property
            mock.assert_called_once()
# end of task 3
