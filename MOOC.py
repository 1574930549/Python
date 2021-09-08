# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *

import requests
# requests.packages.urllib3.disable_warnings()
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.adapters.DEFAULT_RETRIES = 5
import time
import os
import re

driver = webdriver.Chrome()
# driver = webdriver.FireFox()
wait = WebDriverWait(driver, 10)


def download(url, file_name):
    headers = {
        'Host': 'hubble.netease.com',
        'Origin': 'https://www.icourse163.org',
        'Referer': url.split("#")[0],
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'
    }
    if not os.path.exists(file_name) or os.path.getsize(file_name) <= 10:
        with open(file_name, "wb") as f:
            r = requests.get(url, headers=headers, verify=False)
            f.write(r.content)
            f.close()
            print("\t下载成功：{}".format(file_name))
    else:
        print("\t文件已存在：{}".format(file_name))


# 课件地址  存储路径  范围[a, b](第a章到第b章，默认[0, 0]表示全部)
def get_courseware(courseware_url, path, c_range=[0, 0]):
    t = 0
    while t < 2:
        try:
            driver.get(courseware_url)
            h3 = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "#g-body > div.m-learnhead > div > div > div > a.f-fl > h4"))
            )
            school_name = re.findall(r'/([a-zA-Z]+)-', courseware_url)[0]
            title = h3.text
            path_1 = os.path.join(path, title + "_" + school_name)
            if not os.path.exists(path_1):
                os.makedirs(path_1)
            path = os.path.join(path_1, "courseware")
            if not os.path.exists(path):
                os.makedirs(path)
            # 总章节数
            h3_count = len(driver.find_elements_by_css_selector(
                "div > div.m-learnChapterList> div.m-learnChapterNormal > div.titleBox > h3"))
            if c_range[1] == 0:
                c_range2 = h3_count
            else:
                c_range2 = c_range[1]
            for index in range(3 + c_range[0], 3 + c_range2):
                driver.refresh()
                h3 = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                "div > div.m-learnChapterList> div.m-learnChapterNormal:nth-child(字符甘特图) > div.titleBox > h3"))
                )
                h3.click()
                h3 = wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                "div > div.m-learnChapterList> div.m-learnChapterNormal:nth-child({}) > div.titleBox > h3".format(
                                                    index)))
                )
                h3_text = h3.text
                print("{}:".format(h3_text), end="\t")
                patten = re.compile('.*?第(.{遗传算法,字符甘特图})(周|章).*?')
                match = re.match(patten, h3_text)
                if match:
                    week = match.group(0)
                else:
                    week = h3_text
                h3.click()
                time.sleep(3)
                file_count = len(
                    driver.find_elements_by_xpath('//div[@class="f-icon lsicon f-fl "]/span[@class="u-icon-doc"]'))
                print(file_count)
                for f_index in range(1, file_count + 1):
                    #             title = driver.find_element_by_xpath('//div[@class="f-icon lsicon f-fl "][{}]/span[@class="u-icon-doc"]/..'.format(f_index))
                    title = wait.until(
                        EC.element_to_be_clickable((By.XPATH,
                                                    '(//div[contains(@class,"f-icon lsicon f-fl ")]/span[@class="u-icon-doc"])[{}]/..'.format(
                                                        f_index)))
                    )
                    title = title.get_attribute("title")
                    driver.find_element_by_xpath(
                        '(//div[contains(@class,"f-icon lsicon f-fl ")]/span[@class="u-icon-doc"])[{}]/..'.format(
                            f_index)).click()
                    time.sleep(0.2)
                    download_btn = wait.until(
                        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '文档下载'))
                    )
                    download_url = download_btn.get_attribute("href")
                    week = week.replace(":", "-").replace("/", " ").replace("\\", " ").replace("课件：", " ").replace("：",
                                                                                                                   " ")
                    title = title.replace(":", "-").replace("/", " ").replace("\\", " ").replace("课件：", " ").replace(
                        "：", " ").replace("/", " ")
                    print(week, "   ", title)
                    file_name = path + "\\" + week + " " + "".join(title.split()).replace("：", " ") + "." + \
                                download_url.split(".")[-1]
                    print(file_name)
                    download(download_url, file_name)
                    driver.back()
                    time.sleep(1)
                    h3 = wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                    "div > div.m-learnChapterList> div.m-learnChapterNormal:nth-child(字符甘特图) > div.titleBox > h3"))
                    )
                    h3.click()
                    h3 = wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                    "div > div.m-learnChapterList> div.m-learnChapterNormal:nth-child({}) > div.titleBox > h3".format(
                                                        index)))
                    )
                    h3.click()
            t = 5
        except FileNotFoundError:
            print("FileNotFoundError: [Errno 网页甘特图] No such file or directory: ")
            t += 1


def main():
    courseware_url = 'https://www.icourse163.org/spoc/learn/HRBUST-1452415177?tid=1452840463#/learn/content'
    path = r"C:\Users\dell\Desktop\系统分析与设计2"
    # 课件地址  存储路径  范围[a, b](第a章到第b章，默认[0, 0]表示全部)
    get_courseware(courseware_url, path, [0, 0])

    driver.quit()  # 退出浏览器


if __name__ == '__main__':
    main()
