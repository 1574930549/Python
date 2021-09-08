import xlwt

workbook = xlwt.Workbook("test.xlsx")
worksheet = workbook.add_sheet('Sheet1')
for i in range(12):
    for j in range(30):
        worksheet.write(i, j, str(i+1)+'.'+str(j+1))
workbook.save('test.xls')
