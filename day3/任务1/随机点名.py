'''
1.随机点名
  2.随机生成处罚遍数
    技术选型：
        容器类型：
            元组：(1,5,7,4)  不允许做任何修改
            列表：[1,5,7,8,10,41]  可以做任何操作
            字典:{}
列表的方法：通过角标来取值
'''
# #     0  ,1      ,    2 ,    3
# list=[123,321.1321,'aaa',(1,5,7,4)]
# #          数数  0  , 4  交给   i
# for i  in range(0,len(list)):#   len获取一个容器的长度
#     print(list[i])
#任务：循环 ，界面里面有那些人，输入编号指定谁处罚谁就处罚，

import random

list = ["孙佳伟","刘浩","瘦子","特朗普","拜登"]
while True:
    ran = (input("请选择项目：'1'为随机点名, '2'为随机处罚"))
    if ran == "1":
        # 随机生成一个角标
        a = random.choice(list)
        print("恭喜", a)
    elif ran == "2":
        # 随机生成处罚遍数
        print("喜提处罚", random.randint(100, 5000), "遍")
    elif ran == "q" or ran =="Q":
        print("注销成功")
        break
    else:
        break
