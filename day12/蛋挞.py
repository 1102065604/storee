    # 1、需求
    #     3个厨师   6个顾客
    #     有一个篮子可以放500个蛋挞
    #     三个厨师一起做蛋挞，判断篮子满了的话 停3s
    #
    #     每个蛋挞  2元
    #
    #     6个顾客同时抢蛋挞
    #     每人有3000块钱
    #     如果篮子空了 停3秒  再继续抢

from threading import Thread
import time

tart = 0
price = 2

class Chef(Thread):

    def run(self) -> None:
        global tart
        while True:
            if tart >= 50:
                time.sleep(0.001)
            else:
                tart = tart + 1
                time.sleep(0.02)
                print("现在篮子里有：",tart,"个蛋挞")

class customer(Thread):
    money = 300
    count = 0
    name = ""

    def setname(self,name):
        self.name = name

    def run(self) -> None:
        global tart
        global price
        while True:
            if tart < 1:
                time.sleep(0.001)
            elif tart >= 1 and self.money >= price:
                tart = tart - 1
                self.money = self.money - price
                self.count = self.count + 1
                print(self.name, "抢到了一个蛋挞，当前的余额为：", self.money)
            elif self.money < price:
                print(self.name, "余额不足,一共抢了", self.count, "个蛋挞！")
                break

C1 = Chef()
C2 = Chef()
C3 = Chef()

c1 = customer()
c1.setname("大娃")
c2 = customer()
c2.setname( "二娃")
c3 = customer()
c3.setname("三娃")
c4 = customer()
c4.setname("四娃")
c5 = customer()
c5.setname = ("五娃")
c6 = customer()
c6.setname = ("六娃")

C1.start()
C2.start()
C3.start()

c1.start()
c2.start()
c3.start()
c4.start()
c5.start()
c6.start()