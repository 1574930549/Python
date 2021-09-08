import redis
import base64

# 图片转文字

with open("C:\\Users\\zlh\\Desktop\\图片\\Snipaste_2021-04-06_17-22-17.png", "rb") as f:  # 打开01.png图片
    # b64encode是编码，b64decode是解码
    base64_data = base64.b64encode(f.read())  # 读取图片转换的二进制文件，并给赋值
    # base64.b64decode(base64data)
    print(base64_data)
    r = redis.Redis(host='121.89.197.4', port=6379,password=123)
    r.set("jpg_test", base64_data)

    var = r.get("jpg_test")
    print(var)
    data = base64.b64decode(var)  # 把二进制文件解码，并复制给data
    with open("C:\\Users\\zlh\\Desktop\\图片\\jd.jpeg", "wb") as f:  # 写入生成一个jd.png
        f.write(data)