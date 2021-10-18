# F:/自动化测试17/练习的html/上传文件和下拉列表/autotest.html
'''
    下拉选项：
        select组件

'''
from selenium import webdriver
from selenium.webdriver.support.select import Select # 下拉选项
import time

driver= webdriver.Chrome()

driver.get(r"F:/自动化测试17/练习的html/上传文件和下拉列表/autotest.html")
driver.maximize_window()
time.sleep(2)

ele = driver.find_element_by_xpath("//*[@id='areaID']")

st = Select(ele)

st.select_by_value("tianjin")




