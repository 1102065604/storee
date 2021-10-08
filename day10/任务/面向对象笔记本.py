class Computer:
    __screen = ""
    __money = ""
    __cpu = ""
    __ram = ""
    __standby = ""

    def setScreen(self, screen):
        self.__screen = screen

    def getScreen(self):
        return self.__screen

    def setMoney(self, money):
        self.__money = money

    def getMoney(self):
        return self.__money

    def setCpu(self, cpu):
        self.__cpu = cpu

    def getCpu(self):
        return self.__cpu

    def setRam(self, ram):
        self.__ram = ram

    def getRam(self):
        return self.__ram

    def setStandby(self, standby):
        self.__standby = standby

    def getStandby(self):
        return self.__standby

    def use(self, type):
        print("电脑能", type)

    def play(self, game):
        print("电脑能玩", game)

    def watch(self, vedio):
        print("电脑能看", vedio)

    def show(self):
        print("我有一台价值", self.__money, "的，屏幕为", self.__screen, "，内存为", self.__ram,
              "，CPU型号为", self.__cpu, "，待机时长为", self.__standby, "的电脑！")

c = Computer()

c.setScreen("16英寸")
c.setMoney("一万元")
c.setRam("10T")
c.setCpu("i7")
c.setStandby("12小时")

c.use("打字")
c.play("王者荣耀")
c.watch("直播")
c.show()




