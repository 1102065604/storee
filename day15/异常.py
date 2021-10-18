'''
    异常：
        程序在正常运行的过程中出现的非正常情况。
    如何解决？
        try..(监控代码)..except..（具体处理措施）..finally..(疑难杂症)..

'''

li = None

def getValue(li,index):
    return li[index]

try:
    raise SystemError("蓝屏了，蓝瓶的，好喝的！")# 手动抛出异常
    print(getValue(li, 7))
except IndexError:  # 匹配异常
    print("角标错误，请稍后重试！")
except TypeError:
    print("类型异常已解决！哦了！")
except Exception as e:  # Exception是所有异常类的父类
    print("其他异常处理不了，我来兜底！", e.args)




















