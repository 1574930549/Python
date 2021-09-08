import time

import requests
import re
import selenium.webdriver as web
import xlwt
import os
import copy
import threading


def sort(initlist):
    print("sort")
    for each in range(len(initlist)):
        initlist[each] = int(initlist[each])
    initlist = list(set(initlist))
    initlist.sort()
    for each in range(len(initlist)):
        initlist[each] = 'treeZhiBiao_' + str(initlist[each])
    return initlist


def extract_year():
    print("extract_year")
    yearlist = []
    i = 2
    while True:
        try:
            z = driver.find_elements_by_xpath('//*[@id="table_main"]/thead/tr/th[' + str(i) + ']')
            if type(z) == list:
                text = z[0].text
            else:
                text = z.text
            yearlist.append(text)
            i += 1
        except:
            break
    return yearlist


def writeexcel(rootpath, treecode):
    print("Writeexcel")
    excel_name = driver.find_element_by_xpath('//*[@id="' + treecode + '"]').text
    # print("excel_name",excel_name)
    #
    # while True:
    #     try:
    #         print("t")
    #         # str1 = 'treeZhiBiao_' + str(i) + '_ico'
    #         # driver.find_element_by_xpath('//*[@id="' + str1 + '"]').click()
    #         driver.find_element_by_xpath('//*[@id="mySelect_reg"]/div[2]/div[1]').click()
    #         driver.find_element_by_xpath('//*[@id="mySelect_reg"]/div[2]/div[2]/div[2]/ul/li[1]').click()
    #         break
    #     except:
    #         print("f")
    #         # time.sleep(1)
    #         event.wait(1)
    #         print("f2")
    #         continue
    # # time.sleep(2)
    # event.wait(2)
    # countnum = 2
    try:

        # while True:
        #     try:
        #         driver.find_element_by_xpath('//*[@id="mySelect_zb"]/div[2]/div[1]').click()
        #         # time.sleep(2)
        #         event.wait(2)
        #         break
        #     except:
        #         continue
        # excel_name=driver.find_element_by_xpath('//*[@id="mySelect_zb"]/div[2]/div[2]/div[2]/ul/li['+str(countnum)+']').text
        # driver.find_element_by_xpath('//*[@id="mySelect_zb"]/div[2]/div[2]/div[2]/ul/li['+str(countnum)+']').click()
        # # time.sleep(2)
        # event.wait(2)

        yearlist = extract_year()
        while True:
            if yearlist == []:
                break
            else:
                try:
                    checkyear = int(yearlist[0].split('年')[0])
                    if checkyear < 2000:
                        break
                    else:
                        # while True:
                        #     try:
                        #         driver.find_elements_by_xpath('//*[@id="mySelect_sj"]/div[2]/div[1]')[0].click()
                        #         driver.find_elements_by_xpath('//*[@id="mySelect_sj"]/div[2]/div[2]/div[2]/ul/li[3]')[0].click()
                        #         break
                        #     except:
                        #         # time.sleep(1)
                        #         event.wait(1)
                        #         continue
                        yearlist = extract_year()
                        for each in range(len(yearlist)):
                            yearlist[each] = yearlist[each].replace('年', '')  # 将年份的年剔除
                        datadict = {}
                        i = 1  # 数据表的起始点，i代表行的位置
                        data_contain = 0  # 数据总量初始值设为0
                        wk = xlwt.Workbook()  # 建立一个workbook对象
                        sh = wk.add_sheet('sheet1')  # 建立sheet对象，添加表sheet1
                        sh.write(0, 0, '年份')  # 第一行第一列写抬头年份
                        for each in range(len(yearlist)):
                            sh.write(0, each + 1, yearlist[each])
                            # print(yearlist[each])
                            # 第一列除第一行外，年份按yearlist依次读取写入，越往年份小的地方行数越大（each+1代表行，0代表列，注意这里都是从0开始计的！）

                        while True:
                            try:
                                name = \
                                    driver.find_elements_by_xpath(
                                        '//*[@id="table_main"]/tbody/tr[' + str(i) + ']/td[1]')[
                                        0].text
                                # print(name)
                                # y代表列的位置，举例：如果i=1而y=1，则下面的xpath对应的xpath的text是字符串"北京",如果y=2代表的是北京该指标下2019年的数据，y=多少多少往后就是几几年的数据，一一对
                                y = 1
                                while True:
                                    try:
                                        data = driver.find_elements_by_xpath(
                                            '//*[@id="table_main"]/tbody/tr[' + str(i) + ']/td[' + str(y) + ']')[0].text
                                        # print(data)
                                        if data != '':  # 如果该行该列对应的数据不为空，则数据总量加一，否则不加
                                            data_contain += 1
                                            # print("data_contain", data_contain)
                                        else:
                                            pass
                                        try:
                                            sh.write(i, y - 1,
                                                     float(data))  # 注意一下这里统计局的数据的行列和excel表中的行列是转置过来的，因此变换一下y和i的位置
                                        except ValueError:  # 如果出错，代表数据（字符串类型）不能转换为浮点型，这是因为数据是省市的名称，因此直接写入data就行
                                            sh.write(i, y - 1, data)
                                        y += 1
                                    except:  # 此时列已经溢出，try语句出现错误，则break掉列的循环，转而增加i行的个数，在新的i行下爬取数据

                                        break
                                i += 1
                            except:  # 此时行i溢出，已经找不到对应的xpath，因此break掉循环，表的写入结束
                                break
                        if data_contain == 0:  # 如果没有任何数据，则不让它成表（因为没有意义）
                            break
                        else:
                            if '/' in excel_name:  # 同上文解释
                                excel_name = excel_name.replace('/', '每')
                            else:
                                pass
                            wk.save(rootpath + '\\' + excel_name + '.xls')  # 只要data_contain超过0，则将这一指标成表保存
                            print(rootpath + '\\' + excel_name + '.xls写入成功')
                            break  # break掉这一个指标的爬取
                except:
                    break  # 有其他不可预知的错误情况也不让它成表，停止指标爬取
            # countnum += 1  # 进行下一指标项的点击爬取
    except:
        pass  # 已经找不到countnum所在的指标项，因此跳出整个函数，即writeexcel执行完毕


if __name__ == "__main__":
    event = threading.Event()
    os.mkdir('D:\\国家统计局年度数据')
    urla = 'https://data.stats.gov.cn'  # 这里就不从官网进了，因为识别到的也是http形式的，只有https能进去
    req2 = requests.get(urla, verify=False)  # 设置证书认证为关闭状态
    req2.encoding = req2.apparent_encoding
    text2 = req2.text
    match2 = re.compile(r'href=(.*?)? >年度数据')  # 找到分省年度数据的网页url
    answer = re.findall(match2, text2)[0]
    urlb = urla + str(eval(answer))
    option = web.ChromeOptions()
    option.add_argument('--ignore-certificate-errors')  # selenium设置忽略证书的方法
    driver = web.Chrome(options=option)
    driver.get(urlb)
    time.sleep(2)  # 等待网页响应两秒，不然rootname容易读不到数据
    initlist = re.findall(r'treeZhiBiao_([\d]+)', driver.page_source)
    # print(initlist)
    initlist = sort(initlist)
    # initlist.remove(initlist[1])
    copylist = copy.deepcopy(initlist)
    for i in range(1, len(initlist)):
        each = i
        # each = 21

        rootname = driver.find_element_by_xpath('//*[@id="' + initlist[each] + '"]').text
        rootpath = 'D:\\国家统计局年度数据\\' + rootname
        os.mkdir(rootpath)
        while True:
            try:
                driver.find_element_by_xpath('//*[@id="' + str(initlist[each]) + '_ico"]').click()
                break
            except:  # 如果上面的语句click不了用下面的滚动条尝试
                js = 'document.querySelector("#main-container > div.main-left.left.split-containe").scrollTop=10000'
                driver.execute_script(js)
                js2 = 'var action=document.documentElement.scrollTop=10000'
                driver.execute_script(js2)
                # time.sleep(1))#等待程序反应
                event.wait(1)  # 等待程序反应
                continue  # 继续尝试上面的try下面的代码，直到成功break循环
        # time.sleep(5)
        event.wait(5)  # 给予浏览器更新page_source时间
        relist = list(set(re.findall(r'treeZhiBiao_([\d]+)', driver.page_source)))
        relist = sort(relist)  # 去重
        relist.remove(relist[1])  # 整个treeZhiBiao系列的更新
        pathlist = []
        if len(relist) > len(copylist):  # 检验长度是否大于，大于则执行下方代码，否则在最后writeexcel函数解决
            addlist = []
            for i in relist:
                if i not in copylist:
                    addlist.append(i)
                    path = rootpath + ('\\' + driver.find_elements_by_xpath('//*[@id="' + i + '"]')[0].text)
                    # print("test1",driver.find_elements_by_xpath('//*[@id="' + i + '"]')[0].text)
                    pathlist.append(
                        path)  # 将二级节点的路径放入pathlist中，等待后文爬取三级节点并归类时有二级节点的路径参照。这里做了个手脚，如果path当中有同名的，也就是pathlist当中会有同名的，这样两个相同的path下的子文件会被归到一个path下（这里利用了list的全能性，即相同的东西完全不干扰）
                    try:
                        os.mkdir(path)
                        # pass
                    except FileExistsError:  # 出现同名错误则执行以下代码
                        path += '(2)'
                        os.mkdir(path)  # 这里的path+（2）不在pathlist里，自然只是一个躯壳，之后对所有的带（2）的文件夹删除即可
                else:
                    pass
            copylist = relist  # 更新copylist
            while True:
                count = 0  # 对子节点数量进行计数
                addlist2 = []
                pathlist2 = []
                for x in range(len(addlist)):  # 遍历所有addlist
                    treecode = addlist[x]
                    the_path = pathlist[x]
                    # print("treecode",treecode)
                    while True:
                        try:
                            driver.find_element_by_xpath('//*[@id="' + treecode + '_ico"]').click()
                            break
                        except:
                            js = 'document.querySelector("#main-container > div.main-left.left.split-containe").scrollTop=10000'
                            driver.execute_script(js)
                            js2 = 'var action=document.documentElement.scrollTop=10000'
                            driver.execute_script(js2)
                            # time.sleep(1)
                            event.wait(1)
                            continue
                    # time.sleep(4)
                    event.wait(4)  # 滚动条操作等和上文相同
                    relist = list(set(re.findall(r'treeZhiBiao_([\d]+)', driver.page_source)))
                    relist = sort(relist)
                    relist.remove(relist[1])
                    if len(relist) > len(copylist):
                        for y in relist:
                            if y not in copylist:
                                addlist2.append(y)
                                path = the_path  # + ('\\' + driver.find_elements_by_xpath('//*[@id="' + y + '"]')[0].text)
                                # print("ph",path)
                                # print("test",driver.find_elements_by_xpath('//*[@id="' + y + '"]')[0].text)
                                if '/' in path:
                                    path = path.replace('/', '每')  # 替换
                                else:
                                    pass
                                # try:
                                #     pass
                                #     # os.mkdir(path)
                                # except FileExistsError:
                                #     path += '(2)'
                                #     os.mkdir(path)
                                pathlist2.append(path)  # 将子节点的path纳入pathlist2中
                            else:
                                pass
                        count += 1  # 有子节点，count加1，没有不加
                        copylist = relist
                    else:
                        # print("usetreecode",treecode)
                        print("the_path", the_path)
                        writeexcel(the_path, treecode)
                if count == 0:
                    break  # 已经没有任何多出来的子节点，break掉循环，进入下一父节点（第一节点）
                else:
                    pathlist = pathlist2  # 更新pathlist进行下一子结点操作
                    addlist = addlist2  # 更新addlist进行下一子结点操作
                    continue
        else:  # 第一节点数据如果没有子节点时直接爬取右侧表格对应
            writeexcel(rootpath, initlist[each])
            print("rootpath", rootpath)

    driver.close()
