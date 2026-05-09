import unittest
from shipping import get_shipping_cost


class TestShippingCost(unittest.TestCase):
    # 1
    def test_weight_zero(self):
        with self.assertRaises(ValueError) as context:
            get_shipping_cost(0)
        self.assertEqual(str(context.exception), "重量必须大于 0")

    # 2
    def test_weight_just_above_zero(self):
        self.assertEqual(get_shipping_cost(0.01), 10)

    # 3
    def test_weight_two(self):
        self.assertEqual(get_shipping_cost(2), 10)

    # 4
    def test_weight_just_above_two(self):
        self.assertEqual(get_shipping_cost(2.01), 20)

    # 5
    def test_weight_ten(self):
        self.assertEqual(get_shipping_cost(10), 20)

    # 6
    def test_weight_just_above_ten(self):
        self.assertEqual(get_shipping_cost(10.01), 35)

    # 7
    def test_weight_thirty(self):
        self.assertEqual(get_shipping_cost(30), 35)

    # 8
    def test_weight_just_above_thirty(self):
        self.assertEqual(get_shipping_cost(30.01), 50)

    # 9
    def test_weight_fifty(self):
        self.assertEqual(get_shipping_cost(50), 50)

    # 10
    def test_weight_just_above_fifty(self):
        with self.assertRaises(ValueError) as context:
            get_shipping_cost(50.01)
        self.assertEqual(str(context.exception), "重量不能超过 50kg")


if __name__ == '__main__':
    unittest.main()