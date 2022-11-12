from unittest import TestCase
from Calculator import Calculator

class TestCalculator(TestCase):
    def test_c(self):
        calc = Calculator()
        self.assertEqual(0,calc.c())
        calc.sum(1)
        self.assertEqual(0,calc.c())

    def test_sum(self):
        calc = Calculator()
        self.assertEqual(1,calc.sum(1))
        self.assertEqual(3,calc.sum(2))
        self.assertEqual(6,calc.sum(3))
        self.assertEqual(0,calc.c())
        self.assertEqual(1,calc.sum(1))

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(-1, calc.subtract(1))
        calc.sum(3)
        self.assertEqual(0, calc.subtract(2))
        self.assertEqual(-3, calc.subtract(3))
        self.assertEqual(0, calc.c())
        self.assertEqual(-1, calc.subtract(1))

    def test_multiplication(self):
        calc = Calculator()
        self.assertEqual(0,calc.multiplication(1))
        calc.setState(3)
        self.assertEqual(9,calc.multiplication(3))
        self.assertEqual(27, calc.multiplication(3))

    def test_division(self):
        calc = Calculator()
        self.assertEqual(0, calc.division(1))
        calc.setState(3)
        self.assertEqual(3, calc.division(1))
        self.assertEqual(1, calc.division(3))
        self.assertEqual(0.5, calc.division(2))

    def test_percent(self):
        calc = Calculator()
        self.assertEqual(0, calc.percent())
        calc.setState(20)
        calc.multiplication(10)
        self.assertEqual(2, calc.percent())

    def test_sqrt(self):
        calc = Calculator()
        self.assertEqual(0, calc.sqrt())
        calc.setState(4)
        self.assertEqual(2, calc.sqrt())
        calc.setState(81)
        self.assertEqual(9, calc.sqrt())


    def test_pow2(self):
        calc = Calculator()
        self.assertEqual(0, calc.pow2())
        calc.setState(4)
        self.assertEqual(16, calc.pow2())
        self.assertEqual(256, calc.pow2())

    def test_pow(self):
        calc = Calculator()
        self.assertEqual(9, calc.pow(3,2))
        self.assertEqual(27, calc.pow(3,3))
