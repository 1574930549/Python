import requests
import json
import urllib


def getSogouImag(n, path):
    # imgs = requests.get('http://dxs.moe.gov.cn/zx/upload/resources/image/2019/10/29/68570'+n+'.jpeg?1586417668945')
    imgs = 'http://dxs.moe.gov.cn/zx/upload/resources/image/2019/10/29/' + n + '.jpeg?1586417668894'
    urllib.request.urlretrieve(imgs, path + str(n) + '.jpg')
    print('***** ' + str(n) + '.jpg *****' + '   Downloading...')


for n in range(6856979, 6857018):
    getSogouImag(str(n), 'C:/Users/zlh/Desktop/新建文件夹/')
