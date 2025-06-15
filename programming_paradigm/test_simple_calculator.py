from simple_calculator import SimpleCalculator
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(-2, 1), -1)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(-2, 1), -3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(-2, -1), 2)

    def test_division(self):
        self.assertEqual(self.calc.divide(5, 2), 2.5)
