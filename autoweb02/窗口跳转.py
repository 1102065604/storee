from selenium import webdriver
import time

driver= webdriver.Chrome()

driver.get("https://item.jd.com/")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='key']").send_keys("thinkpad  E580")

driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
time.sleep(3)
#  点击详情
driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a').click()
#
# 跳转窗口

# 获取所有窗口句柄
data = driver.window_handles  # ["s001","s002"]

driver.switch_to.window(data[1])

# 点击添加购物车

driver.find_element_by_xpath('//*[@id="InitCartUrl"]').click()













