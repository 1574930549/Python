import requests

url = "https://restapi.amap.com/v3/weather/weatherInfo?city=%E5%93%88%E5%B0%94%E6%BB%A8&key=13cb58f5884f9749287abbead9c658f2"
r = requests.get(url)
print(r.text)
