import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
      
    def setUp(self):
       """set up the SimpleCalculator instance before each test."""
       self.calc = SimpleCalculator()

    def test_addition(self):
       """Test the addition method"""
       self.assertEqual(self.calc.add(2,3), 5)
       self.assertEqual(self.calc.add(-1,1), 0)
       self.assertEqual(self.calc.add(0,0), 0)
       self.assertEqual(self.calc.add(-2,-3), -5)
       self.assertEqual(self.calc.add(1.5,2.5), 4)

    def test_subtraction(self):
          """Test the subtraction method"""
          self.assertEqual(self.calc.subtract(10,5), 5)
          self.assertEqual(self.calc.subtract(5,10), -5)
          self.assertEqual(self.calc.subtract(0,0), 0)
          self.assertEqual(self.calc.subtract(-5,-2), -3)
          self.assertEqual(self.calc.subtract(1.5,0.5), 1)
    
    def test_multipliaction(self):
       """Test the multiplication method"""
       self.assertEqual(self.calc.multiply(4, 5), 20)
       self.assertEqual(self.calc.multiply(0, 10), 0)
       self.assertEqual(self.calc.multiply(-2, 3), -6)
       self.assertEqual(self.calc.multiply(-3, -2), 6)
       self.assertEqual(self.calc.multiply(1.5, 2), 3.0)

    def test_division(self):
       """Test the division method"""
       self.assertEqual(self.calc.divide(10, 2), 5)
       self.assertEqual(self.calc.divide(9, 3), 3)
       self.assertEqual(self.calc.divide(-9, -3), 3)
       self.assertEqual(self.calc.divide(1.5, 0.5), 3)

       #To Test division by zero
       with self.assertRaises(ZeroDivisionError):
          self.calc.divide(10,0)

if __name__ == '__main__':
    unittest.main()