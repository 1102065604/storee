num = int(input("请输入一个整数："))
if num >= 0 and num < 1:
    print("阶乘为0")
if num > 1:
    jiecheng=1
    for i in range(1, num+1):
        jiecheng = jiecheng * i
    print(num, "的阶乘为", jiecheng)