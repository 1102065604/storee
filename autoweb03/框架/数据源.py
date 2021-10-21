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


    wb = xlrd.open_workbook(r"D:\python\pythondaima\autoweb\autoweb03\框架\HKR.xlsx", encoding_override=True)
    st = wb.sheet_by_index(0)
    rows = st.nrows
    da = []
    for j in range(1, rows):
        s1 = st.row_values(j)[0]
        s2 = int(st.row_values(j)[1])
        s3 = st.row_values(j)[2]
        # data=[s1,s2,s3]
        data1 = [{"username": s1, "password": s2, "expect": s3}]
        da.extend(data1)


        # print(data)
    # login_success_data = xlrd.read("HKR.xlsx")

    # login_error_data = [
    #     # id :'msg_uname'
    #     {"username": "jason", "password": "12345678", "expect": "账户名错误或密码错误!别瞎弄!"},
    #     {"username": "jason112234", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"}
    # ]

if __name__ == '__main__':
    da = InitPageData()
    print(da.da)