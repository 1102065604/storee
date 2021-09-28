'''
    1.联网安装pymysql
        python  -m pip  install  pymysql
    2.导入pymysql包
    3.连接数据库
    4.创建控制台
    5.准备一条sql
    6.控制台执行sql语句

    6.1增，删，改
        提交数据
        6.2查询：
            提取数据：
            fetchall()
            fetchone()
            fetchmany(size)
    7.提交到数据库
    8.关闭资源
'''

import pymysql

con = pymysql.connect(host="localhost",user="root",password="root",database="company")

cursor = con.cursor()
# 批量插入数据
sql = "insert into t_dept  value(%s,%s,%s)"

param = [90,'皮革厂','浙江']
# 执行sql
cursor.execute(sql,param)

# 提交到数据
con.commit()

# 关闭资源
cursor.close()
con.close()







































