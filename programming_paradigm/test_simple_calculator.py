# Import the Necessary Modules:

import unittest
from simple_calculator import SimpleCalculator

# Define a Test Class:

class test_simple_calculator(unittest.TestCase):
    def SetUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    
    def test_multiply(self):
        """Test the multiplacation method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 4), 0)


    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(2, 3), 6)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.multiply(0, 4), None)

if __name__ == '__main__':
    unittest.main()        

    
# Use Assertions to Verify Results:    