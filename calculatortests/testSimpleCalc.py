# type run-c-tests to activate the tests 
import unittest
      #folder     # filename              #class
from calculator.simplecalculator import Calculator
from parameterized import parameterized, parameterized_class
     
      # class name     
class TestSimpleCalc(unittest.TestCase):

    def setUp(self):
        print("In setUp() Method")
        # You can set the data here to be used by all test functions
        self.cal = Calculator(4,5)
        self.jake = Calculator(10,5)

    def tearDown(self):
        del self.cal
        del self.jake
        print("In tearDown() Method")


    def test_addition(self):
        # you can also set the data within the function, needs to match the arguments provided by the function you're calling
        self.cal.a = 6
        self.cal.b =84
        self.assertEqual(90, self.cal.add())
        self.assertEqual(15, self.jake.add())
    
    def test_multiplication(self):
        self.assertEqual(20, self.cal.mul())
        self.assertEqual(50, self.jake.mul())
        #almost equal
        self.assertAlmostEqual(47, self.jake.mul(), delta=3)
    
    def test_subtract(self):
        self.assertEqual(-1, self.cal.sub())

    def test_divide(self):
        self.cal.a = 20
        self.cal.b = 2
        self.assertNotEqual(11, self.cal.div())

    def test_assertIs_sub(self):
        self.cal.a = 10
        self.cal.b = 9.2
        self.assertIs(type(9.2), type(self.cal.sub()))
    
    #example of a assertraises error
    def test_division(self):
        #one example
        # self.cal.a = 4
        # self.cal.b = 0
        # self.assertRaises(ZeroDivisionError, self.cal.div)
        #second example
        with self.assertRaises(TypeError):
            self.cal1 = Calculator()

# need this function to run the tests
if __name__=='__main__':
    unittest.main()