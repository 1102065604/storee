# i.人：年龄，性别，姓名。
# ii.现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
# iii.现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。


class person:
    __name = ""
    __age = ""
    __gender = ""

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAge(self, age):
        if 0 < age < 130:
            self.__age = int(age)
        else:
            print("输入非法")

    def setGender(self, gender):
        self.__gender = gender
    def getGender(self):
        return self.__gender

    def work(self,work):
        print(self.__name,"正在认真的",work)

class Worker(person):

    def work(self,work):

        super().work(work)

class student(person):

    grade = ""

    def work(self,work):
        print("学号为：", self.grade, "的")
        super().work(work)

w = Worker()
w.setName("周星驰")
w.setAge(18)
w.setGender("男的")
w.work("投机倒把")


s = student()
s.grade = "180422113"
s.setName("迪丽热巴")
s.setAge(18)
s.setGender("女")
s.work("学习舞蹈")