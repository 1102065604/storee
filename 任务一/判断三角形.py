a = int(input("请输入a = "))
b = int(input("请输入b = "))
c = int(input("请输入c = "))
if (a + b <= c
    or a + c <= b
    or b + c <=a ):
    print("不能够成三角形！")
elif a == b == c:
    print("构成等边三角形")
elif (a == b
      or a == c
      or b == c):
    print("构成等腰三角形")
elif (a ** 2 + b ** 2 ==c ** 2
      or a ** 2 + c ** 2 == b ** 2
      or b ** 2 + c ** 2 == a ** 2):
    print("构成直角三角形")
else:
    print("构成普通三角形")