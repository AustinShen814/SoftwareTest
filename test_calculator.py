import unittest
from calculator import add, is_positive, sqrt, NegativeNumberError


class TestCalculator(unittest.TestCase):
    # 测试1
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 5), 5)

    # 测试2
    def test_is_positive(self):
        self.assertTrue(is_positive(10))
        self.assertTrue(is_positive(0.1))
        self.assertFalse(is_positive(-5))
        self.assertFalse(is_positive(-0.01))
        self.assertFalse(is_positive(0))

    # 测试3
    def test_sqrt(self):
        self.assertAlmostEqual(sqrt(4), 2.0, places=7)
        self.assertAlmostEqual(sqrt(2), 1.414, places=7)

    # 测试4
    def test_sqrt_negative(self):
        with self.assertRaises(NegativeNumberError):
            sqrt(-1)


if __name__ == '__main__':
    unittest.main()