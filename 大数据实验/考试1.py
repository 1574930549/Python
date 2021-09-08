# conding UTF-8
# 中午编码（python3默认中文编码，增强程序可移植性）
import random  # 导包


def ran(zz):  # 定义ran函数
    a = random.randint(10, 99)  # 生成随机数
    b=a
    # b = int(a)  # 类型转换
    if b in zz:  # 判断是否重复
        # print('a')
        ran(zz)  # 重复重新生成随机数
    else:  # 不重复
        for i in range(2, b):  # 从10到i循环
            if b % i == 0:  # 判断是否为素数
                ran(zz)  # 不是素数重新生成随机数
            else:  # 是素数
                return b  # 返回素数
    # return b


if __name__ == '__main__':  # 主函数
    for i in range(0, 100):
        zz = []  # 空列表
        for i in range(0, 10):  # 循环10次
            zz.append(ran(zz))  # 产生非重复两位随机素数并加到列表尾部
        print(zz, end='***')  # 输出并用***结尾
        # for j in range(0, 8):  # 循环8次
        #     print(zz[j], end='***')  # 输出并用***结尾
            # 如果用print(zz[0:8],sep='***')最后一个***将会丢失
        # print(zz[0:8], sep='***')
        print()
