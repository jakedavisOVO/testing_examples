import unittest
from unittest.mock import MagicMock, patch, Mock
from calculator.simplecalculator import Calculator
import calculator.simplecalculator


class myTestCase(unittest.TestCase):

    @unittest.mock.patch('calculator.simplecalculator.Calculator')
    def test_something_mock(self, MockClass):
        instance = MockClass()
        instance.add.return_value = 22
        print(instance.add())
        self.assertEqual(instance.add(), 22)
        assert MockClass is calculator.simplecalculator.Calculator
    
    @unittest.mock.patch('calculator.simplecalculator.Calculator.mul', return_value=76)
    def test_add_2(self, mul):
        ins = Calculator(2,3)
        print(ins.mul())
        self.assertEqual(mul(3,4), 76)


if __name__ == "__main__":
    unittest.main()