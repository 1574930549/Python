import csv
import string
import urllib.request
from bs4 import BeautifulSoup

url = "http://www.weather.com.cn/weather/101050101.shtml"
header = ("User-Agent",
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 "
          "Safari/537.36")  # 设置头部信息
opener = urllib.request.build_opener()  # 修改头部信息
opener.addheaders = [header]  # 修改头部信息
request = urllib.request.Request(url)  # 制作请求
response = urllib.request.urlopen(request)  # 得到请求的应答包
html = response.read()  # 将应答包里面的内容读取出来
html = html.decode('utf-8')  # 使用utf-8进行编码，不重新编码就会成乱码

list1 = []  # 初始化一个空的list，我们为将最终的的数据保存到list
bs = BeautifulSoup(html, "html.parser")  # 创建BeautifulSoup对象
body = bs.body  # 获取body部分
div = body.find('div', {'id': 'curve'})  # 找到id为7d的div
div2 = div.find('em')  # 获取ul部分

# print (li)
i = 0
for day in div2:  # 对每个li标签中的内容进行遍历
    if i < 7:
        date = div2.find('em')  # 找到日期
        print(date)
        i = i + 1
