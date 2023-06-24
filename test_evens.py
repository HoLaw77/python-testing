import unittest


class TestEven(unittest.TestCase):
    def test_function_returns_True(self):
        self.assertTrue(even_numbers_of_evens([]))


unittest.main()
