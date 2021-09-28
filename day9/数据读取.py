'''

    xlrd：读取
    xlwt:写入

    1.打开工作簿
    2.选中选项卡
    3.通过坐标来确定表格
任务1：
    2020年全年的销售统计分析
任务2：
    写个算法，把excel中的数据存在一张表中。
    写个算法，把三国集团的数据，存在Excel表里。
'''

import xlrd

wb = xlrd.open_workbook(filename=r"D:\自动化测试\专项项目\python\xiaoshou\day9\三国集团.xlsx",encoding_override=True)


st = wb.sheet_by_name("用户管理")


rows = st.nrows #  多少行
cols = st.ncols # 多少列
print("有",rows,"行，有",cols,"列")

# for j in range(cols):
#     print(st.col_values(j))


# 统计三国集团总薪资，平均年龄
sum = 0
age_sum = 0
for i in range(1,rows):
    sum = sum + st.row_values(i)[2]
    age_sum =  age_sum + st.row_values(i)[1]

print("总薪资为：￥",sum,"，平均年龄为：",(age_sum // 10))




