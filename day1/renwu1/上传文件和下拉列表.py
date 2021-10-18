from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r"C:/Users/A/Desktop/每日任务/autoweb/day01/练习的html/上传文件和下拉列表/autotest.html")

driver.maximize_window()

driver.find_element_by_xpath("//*[@id='accountID']").send_keys("lu")

driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("123456")

driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")

driver.find_element_by_xpath("//*[@id='sexID1']").click()

driver.find_element_by_xpath("//*[@value='summer']").click()

driver.find_element_by_xpath("//input[@name='file' and @type='file']").send_keys(r"C:\Users\A\Desktop\壁纸.jpg")




