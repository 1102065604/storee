# 生产测试报告
from HTMLTestRunner import HTMLTestRunner  # 界面报告运行，给用户，返回报告
import unittest

# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"D:\自动化测试\专项项目\python\xiaoshou\day13", pattern="Test*.py")



# 2.创建 运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title= "cal",
    description="cal",
    verbosity=1,
    stream = open(file="calc.html",mode="w+",encoding="utf-8")
)

# 3.运行用例
runner.run(tests)


# 4.邮件发送
# 代码的方式发送邮件，报告当成附件发送给我。
# 温馨提示：授权码，不是登陆密码，开启授权码。












