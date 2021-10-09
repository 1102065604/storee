'''
    多线程：
        threading  有个 Thread
    1.子类继承Thread类
    2.重写run方法：写线程的任务代码
    3.启动线程：start()
bypass
'''


from threading import Thread

class PCmanager(Thread):
    def run(self) -> None:
        for i in range(10000):
            print("电脑管家正在杀毒，已经杀了", i ,"个毒！")

class PC360(Thread):
    def run(self) -> None:
        for i in range(10000):
            print("360管家正在杀毒，已经杀了", i ,"个毒！")

p1 =  PCmanager()
p2 =  PC360()

p1.start()
p2.start()

















