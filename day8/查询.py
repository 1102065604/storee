import pymysql

con = pymysql.connect(host="localhost",user="root",password="root",database="bank")

cursor = con.cursor()

sql = "select * from gh  where username = %s"
param = ['鲁皓']
# 执行sql
cursor.execute(sql,param)

# 提取查询数据
data = cursor.fetchmany(3)  # 提取所有查询数据

for i in data:
    print(i)

# 提交到数据
con.commit()

# 关闭资源
cursor.close()
con.close()
