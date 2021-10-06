import pymysql
import xlwt

# 建立数据库连接
con = pymysql.connect(host="localhost",user="root",password="root",database="company")

# 获得游标
cursor = con.cursor()

# 查询表中全部数据，赋值给a
sql = "select * from t_employees"
# 执行sql
cursor.execute(sql)
a = cursor.fetchall()

# 写入表格
wb = xlwt.Workbook()
st = wb.add_sheet("用户管理")

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        st.write(i, j, str(a[i][j]))

# 保存
wb.save("三国集团.xls")

# 关闭资源
cursor.close()
con.close()