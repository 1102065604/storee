'''
    京东，苏宁，淘宝
    登陆使用半自动化来做。



'''



from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r"F:/自动化测试17/练习的html/main.html")

driver.maximize_window()

driver.switch_to.frame("frame")


driver.find_element_by_xpath("//*[@id='input1']").send_keys("jason")





















