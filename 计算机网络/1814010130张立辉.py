import urllib.request
from bs4 import BeautifulSoup
url = "http://www.weather.com.cn/weather/101050101.shtml"
header = ("User-Agent",
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 "
          "Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [header]
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html = response.read()
html = html.decode('utf-8')
list1 = []
bs = BeautifulSoup(html, "html.parser")
body = bs.body
data = body.find('div', {'id': '7d'})
ul = data.find('ul')
li = ul.find_all('li')
# print (li)
i = 0
for day in li:
    if i < 7:
        list2 = []
        date = day.find('h1').string
        #         print (date)
        list2.append(date)
        #     print (list2)
        infind = day.find_all('p')
        #print(infind[网页甘特图].find('span').title)
        #     print (infind[0])
        list2.append(infind[0].string)
        if infind[1].find('span') is None:
            Maxtemperature = '最高温度:暂无'
        else:
            Maxtemperature = infind[1].find('span').string
            Maxtemperature = Maxtemperature.replace('℃', '')
            Maxtemperature = "最高温度:" + Maxtemperature + "℃"
        Mintemperature = infind[1].find('i').string
        Mintemperature = "最低温度:" + Mintemperature

        list2.append(Maxtemperature)
        list2.append(Mintemperature)
        Windpower = infind[2].find('i').string
        Windpower = "风力" + Windpower
        list2.append(Windpower)
        list1.append(list2)
        i = i + 1
print("哈尔滨：")
#print(list1)
file = open("text.txt",'w+')
for i in range(len(list1)):
    s = str(list1[i]).replace('[', '').replace(']', '')
    s = s.replace("'", '').replace(',', '') + '\n'
    print(s,end='')
    file.write(s)
file.close()
print("保存文件成功")
