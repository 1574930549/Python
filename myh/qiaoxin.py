from typing import List
import xlsxwriter


# 读取txt信息函数：
def ReadMatInfo(filepath):
    with open(filepath, 'r') as file:
        data: List[str] = [line.strip() for line in file.readlines()]
        return data


# 将从文件读取的物料X的已确定的MRP进行处理换行符
temp_confirmed_mrp_X = ReadMatInfo('./data_files/MRPConfirmed.txt')[0].split(' ', -1)

# 读取物料X的已确定MRP并加入数组
Confirmed_MRP_X = []
for i in range(len(temp_confirmed_mrp_X) - 1):
    Confirmed_MRP_X.insert(i, int(temp_confirmed_mrp_X[i + 1]))

# 将从文件读取的物料Y的已确定的MRP进行处理换行符
temp_confirmed_mrp_Y = ReadMatInfo('./data_files/MRPConfirmed.txt')[1].split(' ', -1)

# 读取物料Y的已确定MRP并加入数组
Confirmed_MRP_Y = []
for i in range(len(temp_confirmed_mrp_Y) - 1):
    Confirmed_MRP_Y.insert(i, int(temp_confirmed_mrp_Y[i + 1]))

# 将从文件读取的物料X的预测MRP进行处理换行符
temp_pre_mrp_X = ReadMatInfo('./data_files/MRPPredicted.txt')[0].split(' ', -1)

# 读取物料X的预测MRP
Predicted_MRP_X = []
for i in range(len(temp_pre_mrp_X) - 1):
    Predicted_MRP_X.insert(i, int(temp_pre_mrp_X[i + 1]))

# 将从文件读取的物料Y的预测MRP进行处理换行符
temp_pre_mrp_Y = ReadMatInfo('./data_files/MRPPredicted.txt')[1].split(' ', -1)

# 读取物料Y的预测MRP
Predicted_MRP_Y = []
for i in range(len(temp_pre_mrp_Y) - 1):
    Predicted_MRP_Y.insert(i, int(temp_pre_mrp_Y[i + 1]))

# 读取加工车间额定工作能力：

# 读取车间WC01的额定工作能力：
workshop01 = int((ReadMatInfo('./data_files/WCRatedCapacity.txt')[0].split(' ', -1))[1])

# 读取车间WC02的额定工作能力：
workshop02 = int((ReadMatInfo('./data_files/WCRatedCapacity.txt')[1].split(' ', -1))[1])

# 读取文件中工艺路线信息（一共有3条工艺路线）
# 读取第一条工艺路线X1
X1_process_num = int((ReadMatInfo('./data_files/Routing.txt')[0].split(' ', -1))[1])
X1_process_order = int((ReadMatInfo('./data_files/Routing.txt')[0].split(' ', -1))[2])
X1_workshop = (ReadMatInfo('./data_files/Routing.txt')[0].split(' ', -1))[3]
X1_precess_time = int((ReadMatInfo('./data_files/Routing.txt')[0].split(' ', -1))[4])
# 读取第二条工艺路线X2
X2_process_num = int((ReadMatInfo('./data_files/Routing.txt')[1].split(' ', -1))[1])
X2_process_order = int((ReadMatInfo('./data_files/Routing.txt')[1].split(' ', -1))[2])
X2_workshop = (ReadMatInfo('./data_files/Routing.txt')[1].split(' ', -1))[3]
X2_precess_time = int((ReadMatInfo('./data_files/Routing.txt')[1].split(' ', -1))[4])
# 读取第三条工艺路线Y
Y_process_num = int((ReadMatInfo('./data_files/Routing.txt')[2].split(' ', -1))[1])
Y_process_order = int((ReadMatInfo('./data_files/Routing.txt')[2].split(' ', -1))[2])
Y_workshop = (ReadMatInfo('./data_files/Routing.txt')[2].split(' ', -1))[3]
Y_precess_time = int((ReadMatInfo('./data_files/Routing.txt')[2].split(' ', -1))[4])

# 计算过去需求负荷
# 计算WC01的过去需求负载
past_demand_load1 = []
for i in range(len(Confirmed_MRP_X)):
    past_demand_load1.insert(i, Confirmed_MRP_X[i] * X1_precess_time + Confirmed_MRP_Y[i] * Y_precess_time)

# 计算WC02的过去需求负载
past_demand_load2 = []
for i in range(len(Confirmed_MRP_X)):
    past_demand_load2.insert(i, Confirmed_MRP_X[i] * X2_precess_time)

# 计算计划需求负荷
# 计算WC01的计划需求负荷
plan_demand_load1 = []
for i in range(len(Confirmed_MRP_X)):
    plan_demand_load1.insert(i, Predicted_MRP_X[i] * X1_precess_time + Predicted_MRP_Y[i] * Y_precess_time)

# 计算WC02的计划需求负荷
plan_demand_load2 = []
for i in range(len(Confirmed_MRP_X)):
    plan_demand_load2.insert(i, Predicted_MRP_X[i] * X2_precess_time)
# 计算总负荷
# 计算WC01的总负荷
total_load1 = []
for i in range(len(Confirmed_MRP_X)):
    total_load1.insert(i, past_demand_load1[i] + plan_demand_load1[i])

# 计算WC02的总负荷
total_load2 = []
for i in range(len(Confirmed_MRP_X)):
    total_load2.insert(i, past_demand_load2[i] + plan_demand_load2[i])

# 计算平均能力
# 计算WC01的平均能力
average_process_time1 = []
for i in range(len(Confirmed_MRP_X)):
    average_process_time1.insert(i, workshop01)
# 计算WC02的平均能力
average_process_time2 = []
for i in range(len(Confirmed_MRP_X)):
    average_process_time2.insert(i, workshop02)

# 计算余/欠能力
# 计算WC01的余/欠能力
surplus_capacity1 = []
for i in range(len(Confirmed_MRP_X)):
    surplus_capacity1.insert(i, total_load1[i] - average_process_time1[i])

# 计算WC02的余/欠能力
surplus_capacity2 = []
for i in range(len(Confirmed_MRP_X)):
    surplus_capacity2.insert(i, total_load2[i] - average_process_time2[i])

# 计算累计能力
# 计算WC01的累计能力
acc_capacity1 = []
acc_capacity1.insert(0, surplus_capacity1[0])
for i in range(1, len(Confirmed_MRP_X)):
    acc_capacity1.insert(i, surplus_capacity1[i] + surplus_capacity1[i - 1])
# 计算WC02的累计能力
acc_capacity2 = []
acc_capacity2.insert(0, surplus_capacity2[0])
for i in range(1, len(Confirmed_MRP_X)):
    acc_capacity2.insert(i, surplus_capacity2[i] + surplus_capacity2[i - 1])

# 将数据写入到Excel并创建表格
# 创建Excel文档
print("正在进行Excel录入中：")
wb = xlsxwriter.Workbook("./data_files/calculation_of_CRP.xlsx")
# 创建WC01计算结果的表单
ws1 = wb.add_worksheet(name="caculation_of_WC01")
calculation_item = ['过去需求量', '计划需求量', '总负荷量', '平均能力', '余/欠能力', '累计能力']
headline = ['周数', '1', '2', '3', '4', '5', '6']
# 将数据插入到表格中：
ws1.write_row('A1', headline)
ws1.write_column('A2', calculation_item)
ws1.write_row('B2', past_demand_load1)
ws1.write_row('B3', plan_demand_load1)
ws1.write_row("B4", total_load1)
ws1.write_row('B5', average_process_time1)
ws1.write_row('B6', surplus_capacity1)
ws1.write_row('B7', acc_capacity1)

# 创建WC02计算结果的表单
ws2 = wb.add_worksheet(name="caculation_of_WC02")
calculation_item = ['过去需求量', '计划需求量', '总负荷量', '平均能力', '余/欠能力', '累计能力']
headline = ['周数', '1', '2', '3', '4', '5', '6']
# 将数据插入到表格中：
ws2.write_row('A1', headline)
ws2.write_column('A2', calculation_item)
ws2.write_row('B2', past_demand_load2)
ws2.write_row('B3', plan_demand_load2)
ws2.write_row("B4", total_load2)
ws2.write_row('B5', average_process_time2)
ws2.write_row('B6', surplus_capacity2)
ws2.write_row('B7', acc_capacity2)

print("Excel录入完毕！！")
wb.close()

# 在控制台简单输出：
print("WC01结果：")
print("过去需求量是：")
print(past_demand_load1)
print("计划需求量是：")
print(plan_demand_load1)
print("总负荷是：")
print(total_load1)
print("平均能力是：")
print(average_process_time1)
print("余/欠能力是：")
print(surplus_capacity1)
print("累计能力是：")
print(acc_capacity1)

print("WC02结果：")
print("过去需求量是：")
print(past_demand_load2)
print("计划需求量是：")
print(plan_demand_load2)
print("总负荷是：")
print(total_load2)
print("平均能力是：")
print(average_process_time2)
print("余/欠能力是：")
print(surplus_capacity2)
print("累计能力是：")
print(acc_capacity2)