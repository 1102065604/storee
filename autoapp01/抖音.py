from appium import webdriver
import time

remote = "127.0.0.1:4723/wd/hub"

param = {
  "deviceName": "127.0.0.1:62001",
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}

driver = webdriver.Remote(remote, param)
while True:
    time.sleep(10)
    start_x = 300
    start_y = 1000
    distance = 600
    driver.swipe(start_x, start_y, start_x, start_y - distance)
