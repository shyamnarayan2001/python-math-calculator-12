"""Unit tests for calculator module"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers"""
        result = self.calc.add(10, 5)
        self.assertEqual(result, 15)
    
    def test_add_negative_numbers(self):
        """Test addition of negative numbers"""
        result = self.calc.add(-10, -5)
        self.assertEqual(result, -15)
    
    def test_add_mixed_numbers(self):
        """Test addition of positive and negative numbers"""
        result = self.calc.add(-10, 15)
        self.assertEqual(result, 5)
    
    def test_add_float_numbers(self):
        """Test addition of floating-point numbers"""
        result = self.calc.add(25.5, 14.5)
        self.assertEqual(result, 40.0)
    
    def test_add_zero(self):
        """Test addition with zero"""
        result = self.calc.add(10, 0)
        self.assertEqual(result, 10)
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers"""
        result = self.calc.subtract(20, 8)
        self.assertEqual(result, 12)
    
    def test_subtract_negative_numbers(self):
        """Test subtraction of negative numbers"""
        result = self.calc.subtract(-10, -5)
        self.assertEqual(result, -5)
    
    def test_subtract_mixed_numbers(self):
        """Test subtraction with mixed signs"""
        result = self.calc.subtract(10, 30)
        self.assertEqual(result, -20)
    
    def test_subtract_float_numbers(self):
        """Test subtraction of floating-point numbers"""
        result = self.calc.subtract(50.5, 25.3)
        self.assertAlmostEqual(result, 25.2, places=1)
    
    def test_subtract_zero(self):
        """Test subtraction with zero"""
        result = self.calc.subtract(10, 0)
        self.assertEqual(result, 10)
    
    def test_get_result(self):
        """Test get_result method"""
        self.calc.add(10, 5)
        self.assertEqual(self.calc.get_result(), 15)
        
        self.calc.subtract(20, 8)
        self.assertEqual(self.calc.get_result(), 12)


if __name__ == '__main__':
    unittest.main()
