from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
from 工商银行完整版 import *
# username,password,country,province,street,door,money
da = [
    ["jason", "123456", "中国", "安徽省", "桃源铝", "s001", 6000, 1],
    ["jason", "123456", "中国", "安徽省", "桃源铝", "s001", 6000, 2],
    ["jasons1", "123456", "中国", "安徽省", "桃源铝", "s001", 6000, 1],
    ["jasons", "123456", "中国", "安徽省", "桃源铝", "s001", 6000, 3]
]

@ddt
class TestBank(TestCase):

    for i in range(98):
        name = "jason" + str(i)
        bank_addUser(name, "123456", "中国", "安徽省", "桃源铝", "s001", 6000)


    @data(*da)
    @unpack
    def testAddUser(self, a, b, c, d, e, f, g, h):
        s = bank_addUser(a, b, c, d, e, f, g)

        self.assertEqual(h, s)

# 存钱测试
data_save = [
    ["23456789", 5000, False],
    ["21212121", 300, False],
    ["43546578", 300, False]
]

@ddt
class TestBanksave(TestCase):
    @data(*data_save)
    @unpack
    def testSave(self, a, b ,c):
        s = bank_saveMoney(a, b)

        self.assertEqual(c, s)

# 取钱测试
data_take = [
    ["12345432", 123456, 5000, 0],
    ["98767854", 123455, 5000, 0],
    ["84736293", 876567, 5000, 0]
]

@ddt
class TestBanktake(TestCase):
    @data(*data_take)
    @unpack
    def testTake(self, a, b, c, d):
        s = bank_takeMoney(a, b, c)

        self.assertEqual(d, s)

data_trans = [
    ["21345675", "12376890", 123456, 300, 1],
    ["73849023", "18260480", 123456, 300, 1],
    ["20183904", "90346751", 123456, 300, 1],
]

@ddt
class TestBanktrans(TestCase):
    @data(*data_trans )
    @unpack
    def testTrans(self, a, b, c, d, e):
        s = bank_transformMoney(a, b, c, d)
        self.assertEqual(e, s)

data_select = [
    ["19273640", 123456, None],
    ["90283740", 123456, None],
    ["80790650", 123456, None]
]

@ddt
class testBankselect(TestCase):
    @data(*data_select)
    @unpack
    def testSelect(self,a,b, c):
        s = bank_selectUser(a, b)
        self.assertEqual(c, s)






