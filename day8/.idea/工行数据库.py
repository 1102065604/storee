import random
from DBUtils import select
from DBUtils import update

print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank={}
bankname="王者荣耀分行"#全局变量

def bank_adduser(username,password,country,province,street,door,account,money):
    sql = "select count(*) from gh"
    param = []
    data = select(sql, param, mode='one')[0]
    if data >= 100:
        return 3

    sql1 = "select * from gh where username = %s"
    param1 = [username]
    data = select(sql1, param1)
    if len(data) > 0:  # 如果一个变量在容器内就运行代码
        return 2


    sql2 = "insert into gh values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account, username,password, country, province, street, door, money, bankname]
    update(sql2,param2)
    return 1

def useradd():
    username=input("请输入您的用户名：") # 局部变量
    password = input("请输入密码：") # print(bank['Frank']['password'])
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    account=random.randint(10000000,99999999)
    money=0
    useradd=bank_adduser(username,password,country,province,street,door,account,money)
    if useradd == 1:
        print("添加用户成功，以下是您的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：%s
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        sql = 'select money from gh where username= %s'
        param = [username]
        data = select(sql, param, mode='one')[0]
        print(info % (username, account, password, country, province, street, door, data, bankname))
    elif useradd ==2:
        print("用户已存在")
    elif useradd == 3:
        print("数据库已满")

# #存钱逻辑
# def bank_savemoney(account, save_money):
#     if account not in bank:
#         return False
#     else:
#         bank[account]["money"] = bank[account]["money"] + save_money
#         return True

#存钱操作逻辑
def savemoney():
    account_money = input("请输入您的账号：")
    sql = "select * from gh where account = %s"
    param = [account_money]
    data = select(sql, param)
    if len(data) > 0:
        money = int(input("请输入要存款的金额："))
        sql1 = "update  gh set money = money + %s where account = %s"
        param1 = [money, account_money]
        update(sql1, param1)
        sql2 = "select money from gh where account = %s"
        param2 = [account_money]
        data1 = select(sql2, param2, mode = 'one')[0]
        print("存钱成功！当前余额为：", data1)
    else:
        print("用户不存在！")

##取钱逻辑
# def bank_givemoney(account, password, give_money):
#     if account not in bank
#         return 1
#     elif password != bank[account]["password"]:
#         return 2
#     elif give_money > bank[account]["money"]:
#         return 3
#     else:
#         bank[account]["money"] = bank[account]["money"] - give_money
#         return 4

#取钱操作逻辑
def givemoney():
    account = input("请输入您的账号：")
    sql = "select * from gh where account = %s"
    param = [account]
    data = select(sql, param)
    if len(data) > 0:
        while True:
            password = (input("请输入密码："))
            sql1 = "select password from gh where account = %s"
            param1 = [account]
            data1 = select(sql1, param1,mode = 'one')[0]
            if password == data1:
                give_money = int(input("请输入取款金额："))
                sql2 = "select money from gh where account = %s"
                param2 = [account]
                data2 = select(sql2, param2,mode='one')[0]
                if give_money > data2:
                    print("余额不足！", data2)
                else:
                    sql3 = "update gh set money = money - %s where account = %s"
                    param3 = [give_money, account]
                    update(sql3, param3)
                    sql4 = "select money from gh where account = %s"
                    param4 = (account)
                    data3 = select(sql4, param4, mode = 'one')[0]
                    print("取款成功，当前余额为：", data3)
                    break
            else:
                print("密码错误！")
    else:
        print("账号不存在！")

##转账逻辑
# def bank_trans(out_account, in_account, out_password, trans_money):
#     if any([out_account not in bank, in_account not in bank]):
#         return 1
#     elif out_password != bank[out_account]["password"]:
#         return 2
#     elif trans_money >  bank[out_account]["money"]:
#         return 3
#     else:
#         bank[out_account]["money"] = bank[out_account]["money"] - trans_money
#         bank[in_account]["money"] = bank[in_account]["money"] + trans_money
#         return 0

#转账操作逻辑
def transmoney():
    out_account = input("请输入转出账号：")
    sql = "select * from gh where account = %s"
    param = [out_account]
    data = select(sql, param)
    if len(data) > 0:
        in_account = input("请输入转入账号：")
        sql1 ="select * from gh where account = %s"
        param1 = [in_account]
        data1 = select(sql1, param1)
        if len(data1) > 0:
            out_password = input("请输入转出账号密码：")
            sql2 = 'select password from gh where account = %s'
            param2 = [out_account]
            data2 = select(sql2, param2, mode='one')[0]
            while True:
                if out_password == data2:
                    trans_money = int(input("请输入转出金额："))
                    sql3 = "select money from gh where account = %s"
                    param3 = [out_account]
                    data3 = select(sql3, param3, mode='one')[0]
                    if trans_money > data3:
                        print("余额不足，转账失败！")
                        break
                    else:
                        sql4 = "update gh set money = money - %s where account = %s"
                        param4 = [trans_money,out_account]
                        update(sql4, param4)
                        sql5 = "select money from gh where account = %s"
                        param5 = [out_account]
                        data4 = select(sql5, param5, mode = 'one')[0]
                        print("转账成功！您的余额为：", data4)
                        sql6 = "update gh set money = money + %s where account = %s"
                        param6 = [trans_money, in_account]
                        update(sql6, param6)
                        break
                else:
                    print("密码错误！")
        else:
            print("账号不存在！")
    else:
        prrint("账号错误！")

#查询逻辑
def search():
    account = input("请输入要查询的账号：")
    sql = "select * from gh where account = %s"
    param = [account]
    data = select(sql, param)
    if len(data) > 0:
        password = input("请输入要查询的密码：")
        sql1 = 'select password from gh where account = %s'
        param1 = [account]
        data1 = select(sql1, param1, mode='one')[0]
        while True:
            if password == data1:
                sql2 = 'select * from gh where account = %s'
                param2 = [account]
                data2 = select(sql2, param2)
                print(data2)
                break
            else:
                print("密码错误！")
    else:
        print("账号不存在")


    # userExistFlag = False
    # for key, value in bank.items():
    #     #key: username
    #     #value: item
    #     if account == str(value['account']):
    #         userExistFlag = True
    #         if password == value['password']:
    #             print("查询成功！")
    #             info = '''
    #             ------------个人信息------------
    #                     用户名:%s
    #                     账号:%s
    #                     密码:%s
    #                     国籍:%s
    #                     省份:%s
    #                     街道:%s
    #                     门牌号:%s
    #                     余额:%s
    #                     开户行名称:%s
    #             '''
    #             print(info % (key, bank[key]["account"],bank[key]["country"],
    #                         bank[key]["password"], bank[key]["province"], bank[key]["street"],
    #                       bank[key]["door"],bank[key]["money"],bank_name))
    #         else:
    #             print("密码错误！")
    #             return
    # if userExistFlag == False:
    #     print("用户名不存在！")

while True:#永远循环
    begin = input("请选择业务")
    if begin == "1":
        useradd()
    elif begin == "2":
        print("存钱")
        savemoney()
    elif begin == "3":
        print("取钱")
        givemoney()
    elif begin == "4":
        print("转账")
        transmoney()
    elif begin == "5":
        print("查询")
        search()
    elif begin == "6":
        print("退出系统")
        break
    else:
        print("你瞎输入什么东西")
        break