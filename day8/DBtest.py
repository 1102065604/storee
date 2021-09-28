from DBUtils import select
sql = "update  t_employees set sal = sal  -  %s"
param = [1000]

# update(sql,param
sql1 = "select * from t_employees where sal > %s"
param1 = [5000]

data = select(sql1,param1,mode="many",size=3)
for i in data:
    print(i)


















