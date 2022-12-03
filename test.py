import unittest
from generator import prime_generator


class TestPrime(unittest.TestCase):
    def test_prime_generator_1(self):
        res = [i for i in prime_generator(10)]
        expected = [2, 3, 5, 7]
        self.assertEqual(res, expected)

    def test_prime_generator_2(self):
        res = [i for i in prime_generator(1)]
        expected = []
        self.assertEqual(res, expected)

    def test_prime_generator_3(self):
        res = [i for i in prime_generator(100)]
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(res, expected)

if __name__ == "__main__":
    unittest.main()
