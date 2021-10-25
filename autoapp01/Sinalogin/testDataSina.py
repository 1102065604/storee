'''
    任务1：
        自动化刷抖音
    任务2：
        新浪微博登陆自动化框架写出来。
'''

# import time
# from appium import webdriver
# from unittest import TestCase
# from ddt import ddt
# from ddt import data
# from oginPage import Testdata
# from loginOperation import Operation
#
#
# @ddt
# class TestSinaLogin(TestCase):
#
#     def setUp(self) -> None:
#         remote = "127.0.0.1:4723/wd/hub"
#         param = {
#             "deviceName": "127.0.0.1:62001",
#             "platformName": "Android",
#             "platformVersion": "7.1.2",
#             "appPackage": "com.sina.weibo",
#             "appActivity": "com.sina.weibo.SplashActivity"
#         }
#         self.driver = webdriver.Remote(remote, param)
#
#     @data(*Testdata.successData)
#
#     def testsuccess(self, data):
#         # 传入数据
#         username = data['username']
#         expect = data['except']
#
#         lh = Operation(self.driver)
#         lh.successLoginOperation(username)
#
#         result = lh.successLogin_result()
#         time.sleep(2)
#
#         self.assertEqual(expect, result)


from appium import webdriver
from loginData import testData
from loginOperation import Operation
from ddt import ddt
from ddt import data
import time
from unittest import TestCase

@ddt
class TestMain(TestCase):

    def setUp(self) -> None:
        remote = '127.0.0.1:4723/wd/hub'
        prame = {
            "deviceName": "127.0.0.1:62001",
            "platformName": "Android",
            "platformVersion": "7.1.2",
            "appPackage": "com.sina.weibo",
            "appActivity": "com.sina.weibo.SplashActivity"
        }
        self.driver = webdriver.Remote(remote, prame)

    @data(*testData.successfulData)
    def testsuccess(self, data):
        # 传入数据
        username = data['username']
        expect = data['expect']

        jia = Operation(self.driver)
        # 调用操作方法
        jia.successfulOperation(username)

        # 调用判断方法
        result = jia.successful_result()
        time.sleep(5)
        # 断言
        self.assertEqual(expect, result)













