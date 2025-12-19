"""
Unit Tests for Calculator Module
=================================
Comprehensive test suite for the Calculator class.

Author: Narayan
Date: 2025-12-19
"""

import unittest
import sys
import os

# Add parent directory to path to import calculator module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = Calculator()
    
    def tearDown(self):
        """Clean up after each test method."""
        self.calc = None
    
    # Addition Tests
    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)
    
    def test_add_negative_numbers(self):
        """Test addition of two negative numbers."""
        result = self.calc.add(-5, -3)
        self.assertEqual(result, -8)
    
    def test_add_mixed_numbers(self):
        """Test addition of positive and negative numbers."""
        result = self.calc.add(10, -3)
        self.assertEqual(result, 7)
    
    def test_add_floating_point(self):
        """Test addition of floating-point numbers."""
        result = self.calc.add(10.5, 2.3)
        self.assertAlmostEqual(result, 12.8, places=1)
    
    def test_add_zero(self):
        """Test addition with zero."""
        result = self.calc.add(5, 0)
        self.assertEqual(result, 5)
    
    def test_add_large_numbers(self):
        """Test addition of large numbers."""
        result = self.calc.add(1000000, 2000000)
        self.assertEqual(result, 3000000)
    
    # Subtraction Tests
    def test_subtract_positive_numbers(self):
        """Test subtraction of two positive numbers."""
        result = self.calc.subtract(10, 3)
        self.assertEqual(result, 7)
    
    def test_subtract_negative_numbers(self):
        """Test subtraction of two negative numbers."""
        result = self.calc.subtract(-5, -3)
        self.assertEqual(result, -2)
    
    def test_subtract_mixed_numbers(self):
        """Test subtraction with mixed signs."""
        result = self.calc.subtract(5, -3)
        self.assertEqual(result, 8)
    
    def test_subtract_floating_point(self):
        """Test subtraction of floating-point numbers."""
        result = self.calc.subtract(10.5, 2.3)
        self.assertAlmostEqual(result, 8.2, places=1)
    
    def test_subtract_zero(self):
        """Test subtraction with zero."""
        result = self.calc.subtract(5, 0)
        self.assertEqual(result, 5)
    
    def test_subtract_resulting_in_negative(self):
        """Test subtraction resulting in a negative number."""
        result = self.calc.subtract(3, 10)
        self.assertEqual(result, -7)
    
    # History Tests
    def test_history_tracking(self):
        """Test that operations are tracked in history."""
        self.calc.add(5, 3)
        self.calc.subtract(10, 2)
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("5 + 3 = 8", history[0])
        self.assertIn("10 - 2 = 8", history[1])
    
    def test_clear_history(self):
        """Test clearing the operation history."""
        self.calc.add(5, 3)
        self.calc.clear_history()
        history = self.calc.get_history()
        self.assertEqual(len(history), 0)
    
    def test_empty_history_on_init(self):
        """Test that history is empty on initialization."""
        new_calc = Calculator()
        history = new_calc.get_history()
        self.assertEqual(len(history), 0)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
