'''
    专门存储数据源
    任务1：
        使用自动化对HKR系统进行测试。
    任务2：
        将参数化数据集中写到excel表里，并使用excel表参数化。
        将测试结果进行回写到excel表里。
'''
import xlrd



class InitPageData:
    wb = xlrd.open_workbook(r"D:\python\pythondaima\autoweb\autoweb03\登录框架\HKR.xlsx")
    Login_login_data = []
    st = wb.sheet_by_name('login')
    rows = st.nrows
    for i in range(1, rows):
        s = st.row_values(i)
        username = str(s[0])
        passwoed = str(s[1])
        ecpect = str(s[2])
        d = {"username": username, "password": passwoed, "expect": ecpect}
        Login_login_data.append(d)



    Login_error_data = []
    st1 = wb.sheet_by_name('error')
    rows1 = st1.nrows
    for i in range(1, rows1):
        s = st1.row_values(i)
        username = s[0]
        passwoed = int(s[1])
        ecpect = s[2]
        e = {"username": username, "password": passwoed, "expect": ecpect}
        Login_error_data.append(e)

if __name__ == '__main__':
    da1 = InitPageData()
    print(da1.Login_login_data)

if __name__ == '__main__':
    da2 = InitPageData()
    print(da2.Login_error_data)











