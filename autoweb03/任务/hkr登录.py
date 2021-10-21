from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8080/HKR")
driver.maximize_window()

# 跳转到注册页面
time.sleep(3)
driver.find_element_by_xpath("//*[@id='loginname']").send_keys("adminaaa")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='password']").send_keys("admin")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='submit']").click()
time.sleep(1)

# 修改头像
# driver.find_element_by_xpath("//*[@id='img']").click()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@src='img/picture/cat.jpg']").click()

# 评价
# time.sleep(1)
# driver.find_element_by_xpath("//*[@class='tabs-title']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@name='time' and @class='show_tea']").send_keys("9")
driver.find_element_by_xpath("//*[@name='teaName']").send_keys("贾生")
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[5]/td[3]/div/label[1]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[6]/td[2]/div/label[2]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[7]/td[3]/div/label[3]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[8]/td[2]/div/label[4]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[9]/td[2]/div/label[3]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[10]/td[3]/div/label[2]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[11]/td[2]/div/label[1]/div').click()
driver.find_element_by_xpath('//*[@id="form_table"]/tbody/tr[12]/td[2]/div/label[2]/div').click()
driver.find_element_by_xpath('/html/body/div[7]/div[3]/a/span/span').click()


driver.find_element_by_xpath("//*[@id='textarea']").send_keys("无")
driver.find_element_by_xpath("//*[@id='subtn']").click()

# 修改个人信息
time.sleep(1)
driver.find_element_by_xpath("//*[@id='_easyui_tree_8']/span[4]/a").click()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[9]/td[2]/textarea").send_keys("无")
driver.find_element_by_xpath("//*[@id='btn_modify']").click()










