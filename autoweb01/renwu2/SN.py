import time
from selenium import webdriver

# 创建谷歌浏览器对象
driver = webdriver.Chrome()

# 打开苏宁网址
driver.get(r"https://www.suning.com/")

# 窗口最大化
driver.maximize_window()

# 在搜索输入框内查找“一加九Pro”
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("一加九Pro")

# 点击搜索按钮
driver.find_element_by_xpath("//*[@id='searchSubmit']").click()

time.sleep(3)
driver.find_element_by_xpath("//*[@src='//imgservice3.suning.cn/uimg1/b2c/image/33PZXd9p1zoYIPwUyqoHFQ.jpg_400w_400h_4e']").click()

# 跳转界面
d = driver.window_handles
driver.switch_to.window(d[1])

# 延时5秒，查看详情
time.sleep(5)
driver.find_element_by_xpath("//*[@id='addCart']").click()

# 延时5秒，退出浏览器
time.sleep(5)
driver.quit()