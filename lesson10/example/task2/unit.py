import unittest

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class DivideTestCase(unittest.TestCase):
    def test_divide(self):
        result = divide(6, 3)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
