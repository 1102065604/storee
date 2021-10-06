import xlrd


wb = xlrd.open_workbook(filename=r"D:\自动化测试\专项项目\python\xiaoshou\day9\2020年每个月的销售情况.xlsx",encoding_override=True)

# 全年的销售总额
data = 0
for i in range(0, 12):
    st = wb.sheet_by_index(i)
    rows = st.nrows
    cols = st.ncols
    for j in range(1,rows):
        data += st.row_values(j)[2]*st.row_values(j)[4]
print("全年的销售总额为：", data)

# 每种衣服的销售占比
list = ["羽绒服", "牛仔裤", "铅笔裤", "皮草", "衬衫", "卫衣", "T恤", "马甲", "小西装", "休闲裤", "棉衣", "皮衣"]
for m in range(len(list)):
    sum = 0
    data = 0
    for i in range(0, 12):
        st = wb.sheet_by_index(i)
        rows = st.nrows
        cols = st.ncols
        for j in range(1, rows):
            sum += st.row_values(j)[4]
            if st.row_values(j)[1] == list[m]:
                data += st.row_values(j)[4]
    print(list[m], "的销售占比为：", "{:.2%}".format(data/sum))

# 每种衣服的月销售占比
for i in range(0, 12):
    st = wb.sheet_by_index(i)
    rows = st.nrows
    cols = st.ncols
    for m in range(len(list)):
        sum = 0
        data = 0
        for j in range(1, rows):
            sum += st.row_values(j)[4]
            if st.row_values(j)[1] == list[m]:
                data += st.row_values(j)[4]
        print(list[m], i+1, "月销售占比为：", "{:.2%}".format(data/sum))

# 每种衣服的销售额占比
for m in range(len(list)):
    sum = 0
    data = 0
    for i in range(0, 12):
        st = wb.sheet_by_index(i)
        rows = st.nrows
        cols = st.ncols
        for j in range(1, rows):
            sum += st.row_values(j)[4]*st.row_values(j)[2]
            if st.row_values(j)[1] == list[m]:
                data += st.row_values(j)[4]*st.row_values(j)[2]
    print(list[m], "的销售额占比为：", "{:.2%}".format(data/sum))

# 最畅销的衣服
a = 0
sum = 0
for m in range(len(list)):
    sum1 = 0
    data = 0
    for i in range(0, 12):
        st = wb.sheet_by_index(i)
        rows = st.nrows
        cols = st.ncols
        for j in range(1, rows):
            sum1 += st.row_values(j)[4]
            if st.row_values(j)[1] == list[m]:
                data += st.row_values(j)[4]
    if data > sum:
        sum = data
        a = m
print("最畅销的衣服是：", list[a])

# 全年销量最低的的衣服
a = 0
sum = 0
for m in range(len(list)):
    sum1 = 0
    data = 0
    for i in range(0, 12):
        st = wb.sheet_by_index(i)
        rows = st.nrows
        cols = st.ncols
        for j in range(1, rows):
            sum1 += st.row_values(j)[4]
            if st.row_values(j)[1] == list[m]:
                data += st.row_values(j)[4]
    if sum == 0:
        sum = data
    if sum > data:
        sum = data
        a = m
print("全年销量最低的衣服是：", list[a])

# 每个季度的销冠
sum = 0
a = 0
b = 0
c = 0
d = 0
sum1 = 0
sum2 = 0
sum3 = 0
for m in range(len(list)):
    data = 0
    data1 = 0
    data2 = 0
    data3 = 0
    for i in range(12):
        st = wb.sheet_by_index(i)
        rows = st.nrows
        cols = st.ncols
        if 3 <= i <= 5:
            for j in range(1, rows):
                sum1 += st.row_values(j)[4]
                if st.row_values(j)[1] == list[m]:
                    data += st.row_values(j)[4]
            if data > sum:
                sum = data
                a = m
        elif 6 <= i <= 8:
            for j in range(1, rows):
                if st.row_values(j)[1] == list[m]:
                    data1 += st.row_values(j)[4]
            if data1 > sum1:
                sum1 = data1
                b = m
        elif 9 <= i <= 11:
            for j in range(1, rows):
                if st.row_values(j)[1] == list[m]:
                    data2 += st.row_values(j)[4]
            if data2 > sum2:
                sum2 = data2
                c = m
        else:
            for j in range(1, rows):
                if st.row_values(j)[1] == list[m]:
                    data3 += st.row_values(j)[4]
            if data3 > sum3:
                sum3 = data3
                d = m
print('第一个季度最畅销的衣服',list[a])
print('第二个季度最畅销的衣服',list[b])
print('第三个季度最畅销的衣服',list[c])
print('第四个季度最畅销的衣服',list[d])