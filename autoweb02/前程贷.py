from selenium import webdriver
import time
driver = webdriver.Chrome()



driver.get("http://8.129.91.152:8765/")

driver.maximize_window()

driver.find_element_by_xpath("//*[@href='/Index/reg.html']").click()

driver.find_element_by_xpath("//*[@id='phone']").send_keys("13720656044")

time.sleep(8)
driver.find_element_by_xpath("//*[@class='btn btn-success left reget-mobileCode']").click()
time.sleep(3)

text = driver.find_element_by_xpath('//*[@class="layui-layer-content"]')
str = text.text
s = str[len(str)-4:]
driver.find_element_by_xpath("//*[@name='code']").send_keys(s)

driver.find_element_by_xpath("//*[@name='password']").send_keys("lh123456")
driver.find_element_by_xpath("//*[@name='agree']").click()
driver.find_element_by_xpath("//*[@class='btn btn-special']").click()

# 系统自动分配
time.sleep(3)
driver.find_element_by_xpath("//*[@class='layui-layer-btn1']").click()

# 进入实名认证页面
time.sleep(3)
driver.find_element_by_xpath("//*[@src='/Public/frontend/images/personal_center/identity_iden_no.png' and @titel='实名认证']").click()

# 实名认证
time.sleep(3)
driver.find_element_by_xpath("//*[@class='link-color fs-12 right realname-check']").click()
driver.find_element_by_xpath("//*[@name='realname']").send_keys("阿离")
driver.find_element_by_xpath("//*[@name='idcard']").send_keys("140829198609165539")
driver.find_element_by_xpath("//*[@class='btn btn-special']").click()

# 修改手机号
# driver.find_element_by_xpath("//*[@class='link-color fs-12 right verify-phone']").click()
# driver.find_element_by_xpath("//*[@class='btn btn-success left reget-mobileCode']").click()
# time.sleep(3)
# text = driver.find_element_by_xpath('//*[@class="layui-layer-content"]')
# str = text.text
# a = str[len(str)-4:]
# driver.find_element_by_xpath("//*[@name='code']").send_keys(a)








