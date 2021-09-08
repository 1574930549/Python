import openpyxl

filename = r'D:\XZ\test\test.xlsx'
wb = openpyxl.load_workbook(filename)   # 加载表格
sh_name = wb.sheetnames  # 获取所有sheet
sh = wb[sh_name[0]]
sh.title = "Sheet1"  # 修改第一个sheet名为dddd
wb.save(filename) #保存变更
wb.close()