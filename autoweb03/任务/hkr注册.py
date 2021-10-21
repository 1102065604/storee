from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR")
driver.maximize_window()

# 跳转到注册页面
time.sleep(3)
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()

# 输入信息
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("adminaaa")
time.sleep(1)
driver.find_element_by_xpath("//*[@name='username']").send_keys("admin")
time.sleep(1)
driver.find_element_by_xpath("//*[@name='password']").send_keys("admin")
time.sleep(1)
driver.find_element_by_xpath("//*[@name='reloginpass']").send_keys("admin")
time.sleep(1)
driver.find_element_by_xpath("//*[@name='next']").click()
time.sleep(2)

driver.find_element_by_xpath("//*[@name='age']").send_keys("23")
time.sleep(1)
driver.find_element_by_xpath("//*[@name='sex']").send_keys("男")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='classname']").send_keys("测试开发")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()
time.sleep(2)


driver.find_element_by_xpath("//*[@name='email']").send_keys("1102065604@qq.com")
time.sleep(1)
driver.find_element_by_xpath("//*[@name='phoneNumber']").send_keys("13490876453")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/textarea").send_keys("凌霄宝殿")
time.sleep(1)
driver.find_element_by_xpath("//*[@name='submit']").click()

time.sleep(3)
driver.quit()
