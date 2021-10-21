# F:/自动化测试17/练习的html/弹框的验证/dialogs.html
from selenium import webdriver
import time

driver= webdriver.Chrome()

driver.get(r"F:/自动化测试17/练习的html/弹框的验证/dialogs.html")
driver.maximize_window()
time.sleep(2)

driver.find_element_by_xpath("//*[@id='alert']").click()

driver.switch_to.alert.accept() # 点击确定
driver.switch_to.alert.dismiss() # 点击取消














