#任务  判断如果你输入的数字大于随机生成的数字那么给一个提示你猜大了
#                      小于                         小了
#起始资充钱 1000  （账户原有资金+刚充值的资金）10%  2000 20%   每猜一次-500一直执行
#游戏开始按1   退出游戏Q
#资金为0 锁死系统
#5次猜对，5次机会用光了就退出
import  random#随机产生一个数字
ran=random.randint(0,90)#范围(0~90)
print(ran)
coin = 5000
i = 0
while i <=4: #限定次数（5）
    print ("请输入一个数字")
    num = int(input())
    if num>ran :
        coin = coin - 500
        print("你猜大了",coin)
    elif num<ran :
        coin = coin - 500
        print("你猜小了",coin)
    else:
        coin = coin + 5000
        print("ok",coin)
        break
    i = i+1




