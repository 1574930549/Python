import re

import requests
import selenium.webdriver as web
from selenium.webdriver.common.by import By
import redis
from bs4 import BeautifulSoup
url = "https://www.zlh0812.cn/home/"
option = web.ChromeOptions()
option.add_argument('--ignore-certificate-errors')  # selenium设置忽略证书的方法
driver = web.Chrome(options=option)
driver.get(url)
driver.refresh()
# test0 = driver.find_element(By.XPATH,'//*[@id="post-panel"]/div/div[1]/div[2]/h2/a').get_attribute("href")
# print(test0)
for i in range(1,96):
    test0 = driver.find_element(By.XPATH,'//*[@id="post-panel"]/div/div['+str(i)+']/div[2]/h2/a').get_attribute("href")
    print(test0)
# //*[@id="post-panel"]/div/div[1]/div[2]/h2/a
# //*[@id="post-panel"]/div/div[2]/div[2]/h2/a
# //*[@id="post-panel"]/div/div[95]/div[2]/h2/a