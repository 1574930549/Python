import re

import requests
import selenium.webdriver as web
from selenium.webdriver.common.by import By
import redis
from bs4 import BeautifulSoup


def test1(url):
    driver.get(url)
    driver.refresh()
    initlist = re.findall(r'data-id="([\d]+)"', driver.page_source)
    initlist = list(set(initlist))
    print(initlist)

    fburl = []
    str1 = []
    for i in initlist:
        test0 = driver.find_element(By.XPATH,
                                    '//*[@id="feedlist_id"]/li[@data-id="' + str(i) + '"]/div/div/h2/a').get_attribute(
            "href")
        print("url:", test0)
        # fburl.append(test0)
        shi = shijian(test0)
        test1 = driver.find_element(By.XPATH, '//*[@id="feedlist_id"]/li[@data-id="' + str(i) + '"]/div/div').text
        # print(test1,end="")
        try:
            test2 = driver.find_element(By.XPATH, '//*[@id="feedlist_id"]/li[@data-id="' + str(
                i) + '"]/div/dl/div[2]/dd[1]/a/span[2]').text
            # print(test2,end="")
        except:
            test2 = 0
        try:
            test3 = driver.find_element(By.XPATH, '//*[@id="feedlist_id"]/li[@data-id="' + str(
                i) + '"]/div/dl/div[2]/dd[2]/a/span[2]').text
            # print(test3,end="")
        except:
            test3 = 0
        try:
            test4 = driver.find_element(By.XPATH, '//*[@id="feedlist_id"]/li[@data-id="' + str(
                i) + '"]/div/dl/div[2]/dd[3]/a/span[2]').text
            # print(test4,end="")
        except:
            test4 = 0
        test = test1 + "点赞数：" + str(test2) + "浏览量：" + str(test3) + "评论数：" + str(test4) + " 时间" + str(shi)
        print(test)
        cun(i, test)


def shijian(url):
    header = {  # 伪造浏览器头部，不然获取不到网易云音乐的页面源代码。
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Referer': 'http://93.174.95.27',
    }
    data = requests.get(url, headers=header)
    # print("data",data)
    html = data.content
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    songs = soup.find("span", class_="time").text
    # print(songs)
    return songs


def cun(i, test):
    if r.get(i) is not None:
        print("重复")
    else:
        r.set(i, test)


if __name__ == "__main__":
    r = redis.Redis(host='121.89.197.4', port=6379, password="fst13654580966")
    r.flushall()
    url = "https://blog.csdn.net/nav/cloud"
    option = web.ChromeOptions()
    option.add_argument('--ignore-certificate-errors')  # selenium设置忽略证书的方法
    driver = web.Chrome(options=option)
    test1(url)
    test1(url)
    driver.close()
