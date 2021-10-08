# 人类：
#   属性:
#       姓名，性别，年龄，所拥有的手机剩余话费，手机品牌，手机电池容量，手机屏幕大小，手机最大待机
#       时长，所拥有的积分。
#   功能：
#       发短信（要求参数传入短信内容）。
#       打电话（要求传入要打的电话号码和要打的时间长度。程序里判断号码是否为空或者本人的话费是否
#       小于1元，若为空或者小于1元则报相对应的错误信息，否则的话拨通。结束后，按照时间长度扣费并
#       返回扣费（0~10分钟：1元/钟、15个积分/钟，10~20分钟：0.8元/钟、39个积分/钟，
#       其他：0.65元/钟、48个积分/钟））

class Person:
    __username = ""
    __gender = ""
    __age = ""

    # 剩余话费
    __bill = ""

    # 品牌
    __brand = ""

    # 电池容量
    __battery = ""

    # 屏幕尺寸
    __screen = ""

    # 最大待机时长
    __standby = ""

    # 积分
    __intergral = ""

    def setUsername(self, username):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setGender(self, genser):
        self.__gender = genser

    def getGender(self):
        return self.__gender

    def setAge(self, age):
        if 0 < int(age) < 120:
            self.__age = int(age)
        else:
            print("年龄非法！")

    def getAge(self):
        return self.__age

    def setBill(self, bill):
        self.__bill = bill

    def getBill(self):
        return self.__bill

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def setBattery(self, battery):
        if battery < 0:
            print("电池容量不能为负！")
        else:
            self.__battery = battery

    def getBattery(self):
        return self.__battery

    def setScreen(self, screen):
        if int(screen) <= 0:
            print("屏幕大小输入非法！")
        else:
            self.__screen = int(screen)

    def getScreen(self):
        return self.__screen

    def setStandby(self, standby):
        if standby <= 5:
            print("最大待机时长不能为低于5小时！")
        else:
            self.__standby = standby

    def getStandby(self):
        return self.__standby

    def setIntergral(self, intergral):
        if intergral < 0:
            print("积分不能为负！")
        else:
            self.__intergral = intergral

    def getIntergral(self):
        return self.__intergral

    def show(self):
        print("姓名：", self.__username, "\n性别：", self.__gender, "\n年龄：", self.__age, "\n所拥有的剩余话费为：", self.__bill,
              "元\n手机品牌为：", self.__brand, "\n电池容量为：", self.__battery, "\n屏幕尺寸为：", self.__screen, "寸\n最大待机时长"
                "为：", self.__standby, "小时\n所拥有的积分为：", self.__intergral)

p = Person()

p.setUsername(input("请输入姓名:"))
p.setGender(input("请输入性别:"))
p.setAge(input("请输入年龄:"))
p.setBill(input("请输入手机剩余话费:"))
p.setBrand(input("请输入手机品牌:"))
p.setBattery(float(input("请输入电池容量:")))
p.setScreen(input("请输入屏幕尺寸:"))
p.setStandby(int(input("请输入最大待机时长:")))
p.setIntergral(int(input("请输入拥有积分:")))

p.show()

b = p.getBill()
i = p.getIntergral()

while True:
    a = int(input("需要发短信还是打电话：（1或2）"))

    if a == 1:
        a_1 = input("输入短信内容：")
        print("短信内容为：\n", a_1)

    elif a == 2:
        a_1 = int(input("输入电话号码："))
        a_2 = int(input("输入打多长时间："))
        if a_1 == None:
            print("不能为空！")
        elif a_1 <= 1:
            print("电话费不够了！")
        else:
            print("电话已拨通......")

        if 0 <= a_2 <=10:
            if i >= a_2*15:
                i -=a_2*15
            else:
                b -= a_2*1
        elif 10 < a_2 <= 20:
            if i >= a_2*39:
                i -= a_2*39
            else:
                b -= a_2*0.8
        else:
            if i >= a_2*48:
                i -= a_2*48
            else:
                b -= a_2*0.65

        print("剩余话费为：", b)
        print("剩余积分为：", i)

    break