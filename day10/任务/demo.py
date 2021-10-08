'''
    面向过程：
        一般着重研究问题的解决步骤，1，，,,3,4，，,,6
    面向对象：
        研究对象与对象之间处理关系。
        你，贾经理，电脑。
        你指挥贾经理解决一下电脑声卡问题。
        只关心最终的电脑处理结果。
        好处：
            提高开发效率。
            更符合人的思考习惯。
    java：开发网站后台。


    车的图纸-->   车的实物

    自然语言描述车：
        属性：轮胎数，品牌，车身颜色
        行为：跑，拉货

    class Car:
        属性
        行为
    人：
        属性：姓名，年龄，身高
        行为：吃，睡觉，学习，玩游戏
'''
# 类：图纸，模板，蓝图
# 面向过程
def add(a,b):
    return a +b

a = 6
b = 7
add(a,b)

# 面向对象 ： 就是面向过程的变量和行为进行一层封装 --> 类
'''
    封装：
        1.将属性隐藏，不对外进行开放
            __属性
        2.提供方法用于间接赋值。
            setXxx用于赋值，getXxxx用于取值

'''
class  Person:
    __username = ""
    __age = 0
    __high = 0
    __computer = ""

    def setUsername(self,username):
        self.__username = username

    def getUsername(self):
        return self.__username

    def setAge(self,age):
        if age < 0 or age > 120:
            print("年龄非法！别瞎弄！")
        else:
            self.__age = age

    def getAge(self):

        return self.__age

    def setHigh(self,high):
        if high < 0.3  or high > 2.6:
            print("传入的身高，别瞎弄！")
        else:
            self.__high = high
    def getHigh(self):
        return self.__high

    def eat(self,eatname):
        print(self.__username , "正在吃",eatname)

    def sleep(self,hour):
        print(self.__username,"刚学完，睡了",hour,"小时！")

    def study(self,hour):
        print(self.__username,"正在学习，已经学了",hour,"小时！")

    def playGame(self,gamename):
        print(self.__username,"正在玩游戏【",gamename,"】正在启动中...........")

    def showMe(self):
        print("我叫",self.__username,",我今年",self.__age,"岁,我的身高是",self.__high,"米！")

p = Person()  # 实际存在的实体
# p.username = "尉超会"   # 给属性进行赋值
p.setUsername("尉超会")
# p.age = -83  #
p.setAge(83)
# p.high = 1.50
p.setHigh(1.5)


p.eat("猪大肠蜂蜜刺身")  # 调用方法，完成具体功能。
p.study(15)
p.sleep(14)
p.playGame("扫雷")
p.showMe()










class Car:
    num = 0
    brand = ""
    color = ""

    def run(self):
        print(self.brand,"品牌的车在大马路上跑来跑去！")

# a = Car()
#
# a.num = 4
# a.color = "绿色"
# a.brand = "柯尼塞格"
#
# a.run()
#




















