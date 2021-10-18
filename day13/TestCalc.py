'''
    自动测试报告实现了!
    unittest:单元测试框架：
    参数化，测试。
    1.子类继承unittest的TestCase
    2.写用例： testXxxxxx
'''
from unittest import TestCase
from Calc import  Calc
class TestCalc(TestCase):

    # 写第一条用例
    def testAdd1(self):
        # 准备数据
        a = 6
        b = 5
        s = -11
        #
        calc = Calc()
        sum = calc.add(a,b)

        #断言
        self.assertEqual(s,sum)
    # 写第一条用例
    def testAdd2(self):
        # 准备数据
        a = -6
        b = -5
        s = -11
        #
        calc = Calc()
        sum = calc.add(a,b)

        #断言
        self.assertEqual(s,sum)

    # 写第一条用例
    def testAdd3(self):
        # 准备数据
        a = -6
        b = 5
        s = -1
        #
        calc = Calc()
        sum = calc.add(a,b)

        #断言
        self.assertEqual(s,sum)

    # 写第一条用例
    def testAdd4(self):
        # 准备数据
        a = 6
        b = -5
        s = 1
        #
        calc = Calc()
        sum = calc.add(a,b)

        #断言
        self.assertEqual(s,sum)


    # 写第一条用例
    def testAdd5(self):
        # 准备数据
        a = 6000000000000000000000000000000000000000000000000000000000000000000
        b = 5
        s = 6000000000000000000000000000000000000000000000000000000000000000005
        #
        calc = Calc()
        sum = calc.add(a,b)

        #断言
        self.assertEqual(s,sum)


    # 写第一条用例
    def testAdd6(self):
        # 准备数据
        a = 6000000000000000000000000000000000000000000000000000000000000000000
        b = 6000000000000000000000000000000000000000000000000000000000000000000
        s = 12000000000000000000000000000000000000000000000000000000000000000000
        #
        calc = Calc()
        sum = calc.add(a,b)

        #断言
        self.assertEqual(s,sum)













