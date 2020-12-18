# type run-c-tests to activate the tests 
import unittest
from calculator.simplecalculator import Calculator
from parameterized import parameterized, parameterized_class

class myTestCase(unittest.TestCase):
    

    @classmethod
    def setUp(cls):
        cls.cal = Calculator(0, 0)


    @parameterized.expand([
        (1, 1, 2),
        (5, 6, 11),
        (5, 5, 10)
    ])

    def test_add_param(self, in1, in2, out):
        self.cal.a = in1
        self.cal.b = in2
        self.assertEqual(self.cal.add(), out)


if __name__ == "__main__":
    unittest.main()