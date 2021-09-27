# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["曹操", "56", "男", "106", "IBM", 500 , "50"],
    ["大乔", "19", "女", "230", "微软", 501 , "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
a = names[0][5]
b = names[1][5]
c = names[2][5]
d = names[3][5]
avg=((a+b+c+d)/4)
print("平均薪资为", avg)

e = int(names[0][1])
f = int(names[1][1])
g = int(names[2][1])
h = int(names[3][1])
avg1 = ((e+f+g+h)/4)
print("平均薪资为", avg1)

L = [["刘备", "45", "男", "220", "alibaba", 500, "30"]]
names += L
print(names)

names1 = []
for i in names:
    for j in i:
        names1.append(j)
a = names1.count("男")
print("男生出现的次数为", a)
b = names1.count("女")
print("女生出现的次数为", b)

count50 = names1.count("50")
print("50部门的人数为", count50)
count60 = names1.count("60")
print("60部门的人数为", count60)
count10 = names1.count("10")
print("10部门的人数为", count10)