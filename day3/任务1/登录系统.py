count = 0
usename = "root"
usepassword = "admin"
while count < 3:
    name = input("登录账号：")
    password = input("登录密码：")
    if name == usename and password == usepassword:
        print("登陆成功！")
        break
    else:
        print("账号密码不匹配！")
        count = count + 1
else:
    print("您的账号已锁定，请先解锁！")