from selenium import webdriver

# 创建谷歌浏览器对象
driver = webdriver.Chrome()

# 打开跳转页面
driver.get(r"C:/Users/A/Desktop/每日任务/autoweb/day01/练习的html/跳转页面/pop.html")

# # 窗口最大化
driver.maximize_window()

# 跳转
driver.find_element_by_xpath("//*[@id='goo']").click()