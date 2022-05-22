#!/usr/bin/python3
""" Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class TestMaxInteger """

    def test_max_integer(self):
        """ Test Cases """
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 99]), 99)
        self.assertEqual(max_integer([-99, -5, -4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([1, 7, 9, 3, 5, 2]), 9)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([-1, 0]), 0)
        self.assertEqual(max_integer([]), None)
