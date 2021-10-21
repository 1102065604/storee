from selenium import webdriver
import time

# 创建谷歌浏览器对象
driver = webdriver.Chrome()

# 打开京东网址
driver.get(r"https://www.jd.com/")

# 窗口最大化
driver.maximize_window()

# 在搜索输入框内查找“一加九Pro”
driver.find_element_by_xpath("//*[@id='key']").send_keys("一加九Pro")

# 点击搜索按钮
driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a' and @class='button']").click()

# 延时3秒，查看详情
time.sleep(3)
driver.find_element_by_xpath("//*[@src='//img14.360buyimg.com/n7/jfs/t1/198659/36/11950/98053/615ec877E49bbdb7c/6ff0133a60132510.jpg']").click()

# 延时5秒，退出浏览器
time.sleep(5)
driver.quit()