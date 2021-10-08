class Cup:
    __high = ""
    __capacity = ""
    __colo = ""
    __material = ""

    def setHigh(self, high):
        self.__high = high

    def getHigh(self):
        return self.__high

    def setCapacity(self, capacity):
        self.__capacity = capacity

    def getCapacity(self):
        return self.__capacity

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setMaterial(self, material):
        self.__material = material

    def getMaterial(self):
        return self.__material

    def showMe(self):
        print("一个", self.__color, "的",self.__high, "厘米高的", self.__material,
              "材质的水杯，能存放", self.__capacity, "毫升的液体。")



c = Cup()
c.setHigh(15)
c.setCapacity(550)
c.setColor("蓝色")
c.setMaterial("不锈钢")
c.showMe()