"""Unit tests for calculator module."""

import unittest
import sys
import os

# Add parent directory to path to import calculator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10, 20), 30)
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(10, -5), 5)
    
    def test_add_decimal_numbers(self):
        """Test addition of decimal numbers."""
        self.assertAlmostEqual(self.calc.add(5.5, 3.3), 8.8)
        self.assertAlmostEqual(self.calc.add(10.25, 20.75), 31.0)
    
    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 8), 12)
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(10, -5), 15)
    
    def test_subtract_decimal_numbers(self):
        """Test subtraction of decimal numbers."""
        self.assertAlmostEqual(self.calc.subtract(10.5, 3.3), 7.2)
        self.assertAlmostEqual(self.calc.subtract(20.75, 10.25), 10.5)
    
    def test_subtract_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    
    def test_history_tracking(self):
        """Test calculation history tracking."""
        self.calc.add(5, 3)
        self.calc.subtract(10, 4)
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("5 + 3 = 8", history[0])
        self.assertIn("10 - 4 = 6", history[1])
    
    def test_clear_history(self):
        """Test clearing calculation history."""
        self.calc.add(5, 3)
        self.calc.subtract(10, 4)
        self.calc.clear_history()
        self.assertEqual(len(self.calc.get_history()), 0)


if __name__ == '__main__':
    unittest.main()
