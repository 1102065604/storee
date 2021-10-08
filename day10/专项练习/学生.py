# 定义一个学生类和对应的测试类
#   要求：
#   1、学生有姓名和年龄两个属性，并且将属性私有化，提供公有的getXxx与setXxx方法对属性赋值和取值；
#   2、提供一个无返回值的无参数的自我介绍的方法，内容打印一句话：
#    “大家好，我叫xxx，今年xxx岁了！”
#   3、提供一个返回值为String类型，参数为学生类型的比较年龄差值的方法，如果当前对象的年龄比参数中的
#    学生的年龄大，则返回：“我比同桌大xxx岁！”；如果当前对象的年龄比参数中的学生的年龄小，则返回：“
#    我比同桌小xxx岁！”；如果当前对象的年龄和参数中的学生的年龄一样大，则返回：“我和同桌一样大！”
#   4、在测试类中分别创建你和你同桌两个人的对象，并分别给你和你同桌的姓名和年龄属性赋上对应的值；
#   5、调用你自己的对象的自我介绍的方法，展示出你自己的姓名和年龄；
#   6、用你自己的对象调用比较年龄差值的方法，把你同桌作为参数使用，并打印方法返回的字符串的内容；

class Student:
    __username = ""
    __age = ""

    def setUsername(self, username):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setAge(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("年龄非法！")

    def getAge(self):
        return self.__age

    def showme(self):
        print("大家好，我叫", self.__username, "，今年", self.__age, "岁了！")

    # self代表我自己    student代表另一个人
    def compare(self, student):
        if self.__age > student.getAge():
            print("我比同桌大", (self.__age - student.getAge()), "岁！")
        elif self.__age < student.getAge():
            print("我比同桌小", (student.getAge() - self.__age), "岁！")
        else:
            print("我和同桌一样大！")

s = Student()
s.setAge(18)
s.setUsername("可乐")

s1 = Student()
s1.setAge(19)
s1.setUsername("雪碧")

s.showme()
s.compare(s1)
