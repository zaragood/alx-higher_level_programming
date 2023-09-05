#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """runs different testcase"""
    def test_start(self):
        """checks if max number is the first number in the list"""
        max_number = max_integer([9, 2, 4, 1])
        self.assertEqual(max_number, 9)
    
    def test_end(self):
        """checks if max number is the last number in the list"""
        max_number = max_integer([1, 5, 2, 8])
        self.assertEqual(max_number, 8)

    def test_middle(self):
        """checks if max number is the middle number in the list"""
        max_number = max_integer([1, 5, 2, 3])
        self.assertEqual(max_number, 5)

    def test_negetive(self):
        """checks for max number for a list with one negetive value"""
        max_number = max_integer([1, 4, 2, -8])
        self.assertEqual(max_number, 4)

    def test_all_negetive(self):
        """checks for max number in a list with all negetive values"""
        max_number = max_integer([-1, -5, -2, -8])
        self.assertEqual(max_number, -1)

