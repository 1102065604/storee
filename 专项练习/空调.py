# 定义一个空调类和对应的测试类
#   要求：
#   1、空调有品牌和价格两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
#   2、提供一个无返回值的无参数的开机的方法，内容打印一句话：“空调开机了...”；
#   3、提供一个无返回值的带1个int类型参数的定时关机的方法,(int类型的参数表示设定的分钟数)，内容打印一句话：“空调将在xxx分钟后自动关闭...”；
#   4、在测试类中创建出空调对象，并给空调的品牌和价格赋任意值；
#   5、使用空调对象获取空调的品牌和价格并打印到控制台上；
#   6、使用空调对象调用开机方法；
#   7、使用空调对象调用定时关机方法，并传递具体数据值，在控制台上可以看到的效果为：空调将在xxx分钟后自动关闭...
#   其中语句中的“xxx”是调用方法时传递的具体数据值；
class Air:
    __brand = ""
    __price = ""
    __time = ""

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def setRrice(self, price):
        if price < 1000:
            print("价格不能低于100元！")
        else:
            self.__price = price

    def getPrice(self):
        return self.__price

    def setTime(self, time):
        if time <= 0:
            print("时间必须大于0！")
        else:
            self.__time = time

    def start(self):
        print("空调开机了...")

    def shutdown(self):
        print("空调将在",self.__time ,"分钟后自动关闭...")

    def show(self):
        print("我买了一台", self.__brand, "牌的空调，价格为", self.__price, "元，最大能设置为",
              self.__time, "分钟后自动关机！")


a = Air()

a.setBrand("格力")
a.setRrice(3999)
a.setTime(120)

a.start()
a.shutdown()
a.show()