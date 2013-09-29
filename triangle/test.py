'''
Created on Sep 28, 2013

@author: trer
'''
import unittest
import decimal
from triangle import detect_triangle

e = decimal.Decimal('10')**-9
class TestUM(unittest.TestCase):

    def setUp(self):
        pass
    def test0(self):
        self.assertEqual( detect_triangle(3,4,6), "thuong")
    def test1(self):
        self.assertEqual( detect_triangle(2,2,2), "deu")
    def test2(self):
        self.assertEqual( detect_triangle(4,4,6), "can")
    def test4(self):
        self.assertEqual( detect_triangle(4,6,4), "can")
    def test5(self):
        self.assertEqual( detect_triangle(6,4,4), "can")
    def test6(self):
        self.assertEqual( detect_triangle(3,4,5), "vuong")
    def test7(self):
        self.assertEqual( detect_triangle(4,5,3), "vuong")
    def test8(self):
        self.assertEqual( detect_triangle(5,4,3), "vuong")
    def test9(self):
        self.assertEqual( detect_triangle(0,3,5), "wronginput")
    def test10(self):
        self.assertEqual( detect_triangle(3,0,5), "wronginput")
    def test11(self):
        self.assertEqual( detect_triangle(3,5,0), "wronginput")
    def test12(self):
        self.assertEqual( detect_triangle(-1,3,5), "wronginput")
    def test13(self):
        self.assertEqual( detect_triangle(3,-1,5), "wronginput")
    def test14(self):
        self.assertEqual( detect_triangle(3,5,-1), "wronginput")
    def test15(self):
        self.assertEqual( detect_triangle(3,4,8), "khongphaitamgiac")
    def test16(self):
        self.assertEqual( detect_triangle(3,8,4), "khongphaitamgiac")
    def test17(self):
        self.assertEqual( detect_triangle(8,3,4), "khongphaitamgiac")
    def test18(self):
        self.assertEqual( detect_triangle(4,e,4), "can")
    def test19(self):
        self.assertEqual( detect_triangle(e,4,4), "can")
    def test20(self):
        self.assertEqual( detect_triangle(4,4,e), "can")
    def test21(self):
        self.assertEqual( detect_triangle(2**32-1,2**32-3,4),"thuong")
    def test22(self):
        self.assertEqual( detect_triangle(2**32-3,2**32-1,4), "thuong")
    def test23(self):
        self.assertEqual( detect_triangle(2**32-3,4,2**32-1), "thuong")
    def test24(self):
        self.assertEqual( detect_triangle(2**32-1,2**32-1,2**32-1), "deu")
    def test25(self):
        self.assertEqual( detect_triangle(2**32,5,4), "wronginput")
    def test26(self):
        self.assertEqual( detect_triangle(4,2**32,5), "wronginput")
    def test27(self):
        self.assertEqual( detect_triangle(4,5,2**32), "wronginput")
    def test28(self):
        self.assertEqual( detect_triangle(e,e,e),"deu")
if __name__ == '__main__':
    unittest.main()