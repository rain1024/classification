from unittest import TestCase

from model import classify


class TestCategory(TestCase):
    def test_category(self):
        text = "Mở tài khoản ATM thì có đc quà ko ad"
        actual = classify(text)
        expected = "ACCOUNT"
        self.assertEquals(expected, actual)

    def test_category_2(self):
        text = "Cần tư vấn mà add k rep "
        actual = classify(text)
        expected = "CUSTOMER SUPPORT"
        self.assertEquals(expected, actual)

    def test_category_3(self):
        text = "Mình đã đăng nhập thành công. Nhưng ko sử dụng đc các dich vụ. Kể cả xe số dư hay chuyển tiền "
        actual = classify(text)
        expected = ("INTERNET BANKING", "MONEY TRANSFER")
        self.assertEquals(expected, actual)
