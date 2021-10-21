from selenium import webdriver
from unittest import TestCase
import time

class TestHKR(TestCase):


    def testLogin1(self):
        # 准备数据
        username = "jason"
        password = "1234567"
        expect = "Student Login"
        # 打开浏览器操作
        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(1)
        # 获取实际结果
        data = driver.title

        # 关闭浏览器
        driver.quit()


        # 断言

        self.assertEqual(data, expect)

    def testLogin2(self):
        # 准备数据
        username = "不再爱了"
        password = "1234567"
        expect = "Student Login"
        # 打开浏览器操作
        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(1)
        # 获取实际结果
        data = driver.title

        # 关闭浏览器
        driver.quit()
        # 断言
        self.assertEqual(data, expect)



    def testLogin3(self):
        # 准备数据
        username = "不再爱了"
        password = "12345678"
        expect = "账户名错误或密码错误!别瞎弄!"
        # 打开浏览器操作
        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(1)
        # 获取实际结果
        data = driver.find_element_by_xpath("//*[@id='msg_uname']").text

        # 关闭浏览器
        driver.quit()
        # 断言
        self.assertEqual(data, expect)








































