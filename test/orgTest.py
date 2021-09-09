import unittest

from main import test

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(test("words1.txt", "org1.txt", "")[0], "Line1: <法轮功> FaLG")

    def test2(self):
        self.assertEqual(test("words1.txt", "org2.txt", "")[0], "Line1: <法轮功> 法轮功")

    def test3(self):
        self.assertEqual(test("words1.txt", "org3.txt", "")[0], "Line1: <法轮功> falungong")

    def test4(self):
        self.assertEqual(test("words1.txt", "org4.txt", "")[0], "Line1: <法轮功> 发论共")

    def test5(self):
        self.assertEqual(test("words1.txt", "org5.txt", "")[0], "Line1: <法轮功> fa论g")

    def test6(self):
        self.assertEqual(test("words1.txt", "org6.txt", "")[0], "Line1: <法轮功> 法论****共")

    def test7(self):
        self.assertEqual(test("words1.txt", "org7.txt", "")[0], "Line1: <法轮功> flg")

    def test8(self):
        self.assertEqual(test("words1.txt", "org8.txt", "")[0], "Line1: <法轮功> 发论gong")

    def test9(self):
        self.assertEqual(test("words1.txt", "org9.txt", "")[0], "Line1: <法轮功> 发伦***共")

    def test10(self):
        self.assertEqual(test("words1.txt", "org10.txt", "")[0], "Line1: <法轮功> fa伦12共")


if __name__ == '__main__':
    unittest.main()
