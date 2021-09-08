import xlrd
import xlwt


def read():
    data1 = xlrd.open_workbook(r'C:\Users\zlh\Desktop\数据分析方法实验\实验一、二\实验一数据\wine1.xlsx')
    sheet1 = data1.sheet_names()
    table1 = data1.sheet_by_name(sheet1[0])

    data2 = xlrd.open_workbook(r'C:\Users\zlh\Desktop\数据分析方法实验\实验一、二\实验一数据\wine2.xlsx')
    sheet2 = data2.sheet_names()
    table2 = data2.sheet_by_name(sheet2[0])

    Alcohol = table1.col_values(1)
    del Alcohol[0]
    # print(Alcohol)
    Weight = table1.col_values(5)
    del Weight[0]
    Proline = table2.col_values(8)
    del Proline[0]
    return table1, table2, Alcohol, Weight, Proline


def write(table1, table2, Alcohol, Weight, Proline, p, a):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Sheet1')

    for i in range(table1.ncols):
        for j in range(table1.nrows):
            worksheet.write(j, i, label=table1.cell(j, i).value)
    for i in range(1, table2.ncols):
        for j in range(table2.nrows):
            worksheet.write(j, i + table1.ncols - 1, label=table2.cell(j, i).value)

    Quality = ["Quality"]
    for i in range(len(Alcohol)):
        n = Alcohol[i] / Weight[i]
        Quality.append(n)

    for j in range(table2.nrows):
        worksheet.write(j, 14, label=p[j])
        worksheet.write(j, 15, label=a[j])
        worksheet.write(j, 16, label=Quality[j])

    workbook.save('Wine.xls')


def Standardization(Alcohol, Proline):
    Proline_min = min(Proline)
    Proline_max = max(Proline)
    Alcohol_min = min(Alcohol)
    Alcohol_max = max(Alcohol)
    # print(Proline_min)
    # print(Proline_max)
    # print(Alcohol_min)
    # print(Alcohol_max)
    Alcohol_Standardization = ['Alcohol_Standardization']
    Proline_Standardization = ['Proline_Standardization']
    for i in range(len(Alcohol)):
        num = (Alcohol[i] - Alcohol_min) / (Alcohol_max - Alcohol_min)
        Alcohol_Standardization.append(num)
        # print(num)
    for i in range(len(Proline)):
        num = (Proline[i] - Proline_min) / (Proline_max - Proline_min)
        Proline_Standardization.append(num)
        # print(num)
    return Proline_Standardization, Alcohol_Standardization


if __name__ == "__main__":
    table1, table2, Alcohol, Weight, Proline = read()
    p, a = Standardization(Alcohol, Proline)
    write(table1, table2, Alcohol, Weight, Proline, p, a)
