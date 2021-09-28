import xlwt

wb = xlwt.Workbook()

st = wb.add_sheet("薪资管理")

st.write(0,0,"5000")

wb.save("薪资管理.xls")








