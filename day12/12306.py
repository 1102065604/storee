'''
    1.需求：
        500张票
        3个人同时在抢票。抢的谁算谁的。
    接口 + 多线程：
'''
from threading import Thread
import time
 # 票池
ticket = 500000

class Person(Thread):
    username = ""
    count = 0 # 票的计数器
    def run(self) -> None:
        global ticket
        while True:
            if ticket > 0:
                self.count = self.count + 1
                ticket = ticket - 1
                # print(self.username,"成功抢了一张票！还剩",ticket,"张！")

            else:
                print(self.username,"总共抢了",self.count,"张票!")
                break

p1 = Person()
p2 =Person()
p3 = Person()
p1.username = "孙佳玮"
p2.username = "尉超会"
p3.username = "jason jia"

p1.start()
p2.start()
p3.start()





















