'''
Created on Sep 25, 2013

@author: Admin
'''
import unittest
from triangle import detect_triangle
import math

class Test(unittest.TestCase):
    
    def testKhoangGiaTriCanh1(self):
        self.assertEqual(detect_triangle(2**32, 2, 2), 'dau vao khong hop le')
    def testKhoangGiaTriCanh2(self):
        self.assertEqual(detect_triangle(2, 2**32, 2), 'dau vao khong hop le')    
    def testKhoangGiaTriCanh3(self):
        self.assertEqual(detect_triangle(2, 2, 2**32), 'dau vao khong hop le')
    def testKhoangGiaTriCanh4(self):
        self.assertEqual(detect_triangle(2**32, 2**32, 2**32), 'dau vao khong hop le')
    def testKieuA(self):
        self.assertEqual(detect_triangle('ad', 4.0, 5.0), 'dau vao khong hop le') 
    def testKieuB(self):
        self.assertEqual(detect_triangle(4, 'a', 5.0), 'dau vao khong hop le')
    def testKieuC(self):
        self.assertEqual(detect_triangle(1, 4.0, 'a'), 'dau vao khong hop le') 
    def testKieuABC(self):
        self.assertEqual(detect_triangle('a', 'a', 'a'), 'dau vao khong hop le') 
    def testThamSoAm1(self):
        self.assertEqual(detect_triangle(-4, -5, -5), 'dau vao khong hop le')
    def testThamSoAm2(self):
        self.assertEqual(detect_triangle(-4, 5, 5), 'dau vao khong hop le')
    def testThamSoAm3(self):
        self.assertEqual(detect_triangle(4.22, -5, 5), 'dau vao khong hop le')
    def testThamSoAm4(self):
        self.assertEqual(detect_triangle(4.22, 5, -5), 'dau vao khong hop le')
    def testKoLaTamGiac(self):
        self.assertEqual(detect_triangle(2, 3, 5),'khong la tam giac')
    def testTamGiacCan1(self):
        self.assertEqual(detect_triangle(2**32-2, 2**32-2, 5), 'tam giac can')
    def testTamGiacCan2(self):
        self.assertEqual(detect_triangle(3, 5, 3), 'tam giac can')
    def testTamGiacCan3(self):
        self.assertEqual(detect_triangle(5.22, 3.22, 3.22), 'tam giac can')
    def testTamGiacDeu(self):
        self.assertEqual(detect_triangle(3, 3, 3), 'tam giac deu')
    def testTamGiacVuong1(self):
        self.assertEqual(detect_triangle(3, 4, 5), 'tam giac vuong')
    def testTamGiacVuong2(self):
        self.assertEqual(detect_triangle(4, 3, 5), 'tam giac vuong')
    def testTamGiacVuong3(self):
        self.assertEqual(detect_triangle(5, 4, 3), 'tam giac vuong')
    def testTamgiacVuongCan1(self):
        self.assertEqual(detect_triangle(1, 1, math.sqrt(2)), 'tam giac vuong can')
    def testTamgiacVuongCan2(self):
        self.assertEqual(detect_triangle(1, math.sqrt(2),1), 'tam giac vuong can')
    def testTamgiacVuongCan(self):
        self.assertEqual(detect_triangle(math.sqrt(2),1,1), 'tam giac vuong can')
    def testTamGiacThuong(self):
        self.assertEqual(detect_triangle(2, 3, 4), 'tam giac thuong')
    def testEspescial(self):
        self.assertEqual(detect_triangle(2**32-2, 2**3, 2**32-1), 'tam giac thuong')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()