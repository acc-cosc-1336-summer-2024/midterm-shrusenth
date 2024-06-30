#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import get_sum_of_evens


class Test_Config(unittest.TestCase):
    def test_sum_of_evens_11(self):
        self.assertEqual(get_sum_of_evens(11), 30)
    def test_sum_of_evens_10(self):
        self.assertEqual(get_sum_of_evens(10), 30)
    def test_sum_of_evens_8(self):
        self.assertEqual(get_sum_of_evens(8), 20)
    

from src.question_b.question_b import get_fahrenheit

class Test_Config(unittest.TestCase):
     
    def test_fahrenheit_for_0(self):
        self.assertEqual(get_fahrenheit(0), 32)

    def test_fahrenheit_for_5(self):
        self.assertEqual(get_fahrenheit(5), 41)
    
    def test_fahrenheit_for_10(self):
        self.assertEqual(get_fahrenheit(10), 50)
    

from src.question_c.question_c import is_prime

class TestIsPrime(unittest.TestCase):
    
    def test_prime_4(self):
        self.assertFalse(is_prime(4))

    def test_prime_5(self):
        self.assertTrue(is_prime(5))

    def test_prime_11(self):
        self.assertTrue(is_prime(11))

from src.question_d.question_d import get_day_of_week

class Test_Config(unittest.TestCase):

    def test_day_0(self):
        self.assertEqual(get_day_of_week(0), "Invalid number. Please enter a number between 1 and 7.")

    def test_day_1(self):
        self.assertEqual(get_day_of_week(1), "Monday")

    def test_day_2(self):
        self.assertEqual(get_day_of_week(2), "Tuesday")

    def test_day_3(self):
        self.assertEqual(get_day_of_week(3), "Wednesday")

if __name__ == "__main__":
    unittest.main()
    
