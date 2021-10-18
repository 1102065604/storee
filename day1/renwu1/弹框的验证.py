from selenium import webdriver
import time


# 创建谷歌浏览器对象
driver = webdriver.Chrome()

# 打开弹框的验证页面
driver.get(r"C:/Users/A/Desktop/每日任务/autoweb/day01/练习的html/弹框的验证/dialogs.html")

# 窗口最大化
driver.maximize_window()


driver.find_element_by_xpath("//*[@id='alert']").click()

# driver.find_element_by_xpath("//*[@id='confirm']").click()

# 延时3秒
time.sleep(3)
# 退出浏览器
driver.quit()