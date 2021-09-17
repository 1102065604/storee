list = ["36710.36", "35427.10", "29863.23", "29667.39", "27665.36", "27650.45", "27620.38", "25369.20"]
sum = 0
avg = 0
for i in range(0, len(list)):
    sum = sum + float(list[i])
print("GDP总和为",sum)
avg = len(list)
print("平均GDP为", sum/avg)
