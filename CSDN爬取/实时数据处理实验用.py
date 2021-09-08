import time
import selenium.webdriver as web
import xlwt

from selenium.webdriver.common.by import By

# workbook = xlwt.Workbook("test.xlsx")
# worksheet = workbook.add_sheet('Sheet1')
f=open("test.txt","w+",encoding='utf-8')
js_bottom = "var q=document.documentElement.scrollTop=10000"
url = "https://blog.csdn.net/sunxianghuang"
option = web.ChromeOptions()
option.add_argument('--ignore-certificate-errors')  # selenium设置忽略证书的方法
driver = web.Chrome(options=option)
driver.get(url)
driver.execute_script(js_bottom)
time.sleep(3)
print(driver)
for i in range(1, 10):
    driver.execute_script("var q=document.documentElement.scrollTop=" + str(i * 10000))
    time.sleep(2)
for i in range(1, 140):
    try:
        print(i, end="")
        label2 = driver.find_element(By.XPATH,
                                     '//*[@id="floor-user-profile_485"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[' + str(
                                         i) + ']/article/a/div[1]').text
        # print(label2, end="")
        print(label2)
        f.write(label2)
        f.write("\r")
        # worksheet.write(i - 1, 0, label2)
        # label3 = driver.find_element(By.XPATH,
        #                              '//*[@id="floor-user-profile_485"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[' + str(
        #                                  i) + ']/article/a/div[3]/div[1]/div[2]/span').text
        # print(label3, end="")
        # worksheet.write(i - 1, 1, label3)
        # label4 = driver.find_element(By.XPATH,
        #                              '//*[@id="floor-user-profile_485"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[' + str(
        #                                  i) + ']/article/a/div[3]/div[1]/div[3]/span').text
        # print(label4, end="")
        # worksheet.write(i - 1, 2, label4)
        # label5 = driver.find_element(By.XPATH,
        #                              '//*[@id="floor-user-profile_485"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[' + str(
        #                                  i) + ']/article/a/div[3]/div[1]/div[4]/span').text
        # print(label5, end="")
        # worksheet.write(i - 1, 3, label5)
        #
        # label6 = driver.find_element(By.XPATH,
        #                              '//*[@id="floor-user-profile_485"]/div/div[2]/div/div[2]/div/div[2]/div/div/div[' + str(
        #                                  i) + ']/article/a/div[3]/div[2]').text
        # print(label6)
        # worksheet.write(i - 1, 4, label6)
    except:
        # worksheet.write(i - 1, 0, "MISS")
        continue
# workbook.save('test.xls')
f.close()
driver.close()
