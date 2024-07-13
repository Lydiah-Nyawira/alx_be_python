# Import the Necessary Modules:

import unittest
from simple_calculator import SimpleCalculator

# Define a Test Class:

class testSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

# Write test methods
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 4), 0)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(2, 3), 0.6666666666666666)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 4), 0)