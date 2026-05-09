import unittest
from check_age import check_age


class TestCheckAge(unittest.TestCase):

    # 测试未成年分支
    def test_underage(self):
        self.assertEqual(check_age(0), "未成年")
        self.assertEqual(check_age(17), "未成年")
        self.assertEqual(check_age(10.5), "未成年")

    # 测试成年分支
    def test_adult(self):
        self.assertEqual(check_age(18), "成年")
        self.assertEqual(check_age(30), "成年")
        self.assertEqual(check_age(60), "成年")

    # 测试老年分支
    def test_elderly(self):
        self.assertEqual(check_age(61), "老年")
        self.assertEqual(check_age(100), "老年")
        self.assertEqual(check_age(80.5), "老年")


if __name__ == '__main__':
    unittest.main()