from selenium import webdriver
from unittest import TestCase
from ddt import ddt
from ddt import data
from autoweb03.登录框架.InitPage import InitPageData
from autoweb03.登录框架.LoginOperation import LoginOpera
import time
from 读取 import Write_excel
from 读取 import Write_excel1


'''
    成功的用例
    失败的用例
'''
m = 1
n = 1
@ddt
class TestLogin(TestCase):
    #在每个测试用例执行前执行
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/HKR")
        self.driver.maximize_window()

    # 在每个用例执行后执行
    def tearDown(self) -> None:
        self.driver.quit()


    # 登陆成功的用例
    @data(*InitPageData.Login_login_data)
    def testLoginSuccess(self, testdata):
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]

        # time.sleep(2)
        loginopr = LoginOpera(self.driver)
        #  登陆的三项操作
        loginopr.login(username, password)

        result = loginopr.getSuccess_result()
        time.sleep(2)

        global m
        table1 = Write_excel(r"D:\python\pythondaima\autoweb\autoweb03\登录框架\HKR.xlsx")
        if result == expect:
            table1.write1(m + 1, 4, "pass")
        else:
            table1.write1(m + 1, 4, "fail")
        m += 1

        # 断言
        self.assertEqual(result, expect)


    # 登陆失败的用例
    @data(*InitPageData.Login_error_data)
    def testLoginError(self, testdata):
        username = testdata["username"]
        password = testdata["password"]
        expect = testdata["expect"]
        # time.sleep(2)
        loginopr = LoginOpera(self.driver)
        #  登陆的三项操作
        loginopr.login(username, password)

        result = loginopr.getError_result()
        time.sleep(2)

        global n
        table = Write_excel1(r"D:\python\pythondaima\autoweb\autoweb03\登录框架\HKR.xlsx")
        if result == expect:
            table.write1(n + 1, 4, "pass")
        else:
            table.write1(n + 1, 4, "fail")
        n += 1

        # 断言
        self.assertEqual(result, expect)


























