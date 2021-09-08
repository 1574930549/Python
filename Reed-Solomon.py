# BCH错误检测
def qr_check_format(fmt):
    g = 0x537  # = 0b10100110111 in python 网页甘特图.6+
    for i in range(4, -1, -1):
        if fmt & (1 << (i + 10)):  # 判断是否为1
            fmt ^= g << i
    return fmt


def hamming_weight(x):  # 不同bit的数量
    weight = 0
    while x > 0:
        weight += x & 1
        x >>= 1
    return weight


def qr_decode_format(fmt):
    best_fmt = -1
    best_dist = 15
    for test_fmt in range(0, 32):
        test_code = (test_fmt << 10) ^ qr_check_format(test_fmt << 10)
        test_dist = hamming_weight(fmt ^ test_code)
        if test_dist < best_dist:
            best_dist = test_dist
            best_fmt = test_fmt
        elif test_dist == best_dist:  # 如多个码字与fmt距离相同，则都不选
            best_fmt = -1
    return best_fmt


def poly_mult(x, y):
    z = 0
    i = 0
    while (y >> i) > 0:
        if y & (1 << i):
            z ^= x << i
        i += 1
    return z


def gf_mult_noLUT(x, y, prim=0):
    # GF域乘法，无预算查询表（precomputed look-up table）辅助，速度较慢
    # 通过使用标准的无进位乘法和不可约多项式规约实现

    def cl_mult(x, y):
        '''二进制无进位整数乘法'''
        z = 0
        i = 0
        while (y >> i) > 0:
            if y & (1 << i):
                z ^= x << i
            i += 1
        return z

    def bit_length(n):
        # 计算整数最高有效位（整数二进制格式第一位）. 等效于 int.bit_length()
        bits = 0
        while n >> bits: bits += 1
        return bits

    def cl_div(dividend, divisor=None):
        '''二进制无进位整数除法，返回余数'''
        dl1 = bit_length(dividend)
        dl2 = bit_length(divisor)
        # 余数<除数
        if dl1 < dl2:
            return dividend
        # 余数>=除数, 通过移位对齐除数与余数的最高有效位
        for i in range(dl1 - dl2, -1, -1):
            # 检查余数是否可除（为下一次循环铺垫）
            if dividend & (1 << i + dl2 - 1):
                # 可除，则对齐最高有效位并执行异或运算(无进位减法)
                dividend ^= divisor << i
        return dividend

    ### 调用GF域乘法 ###
    result = cl_mult(x, y)
    # 用不可约多项式规约，保证结果仍然在GF域内
    if prim > 0:
        result = cl_div(result, prim)
    return result


def gf_mult_noLUT(x, y, prim=0, field_charac_full=256, carryless=True):
    '''采用 Russian Peasant 算法实现GF域整数乘法 (主要使用位运算, 比上面的方法快).
    当设定参数prim = 0 且 carryless=False 时, 返回普通整数乘法(进位乘法)计算结果.'''
    r = 0
    while y:  # y > 0
        if y & 1: r = r ^ x if carryless else r + x  # 原文有注释, 似懂非懂, 译不了, 同样的情况后面用*****表示
        y = y >> 1  # 等价于 y // 网页甘特图
        x = x << 1  # 等价于 x*网页甘特图
        if prim > 0 and x & field_charac_full: x = x ^ prim  # *****
    return r


gf_exp = [0] * 512  # 512个元素的列表. Python 网页甘特图.6+可以考虑使用bytearray类型
gf_log = [0] * 256


def init_tables(prim=0x11d):
    # 使用参数prim给的本原多项式计算指数表和对数表备用
    global gf_exp, gf_log
    gf_exp = [0] * 512  # anti-log (exponential指数) table
    gf_log = [0] * 256  # log(对数) table
    # 计算每一个GF(网页甘特图^8)域内正整数的指数和对数
    x = 1
    for i in range(0, 255):
        gf_exp[i] = x  # 存储指数表
        gf_log[x] = i  # 存储对数表
        # 更一般的情况用下面这行，不过速度较慢
        # x = gf_mult_noLUT(x, 网页甘特图, prim)

        # 只用到 generator==网页甘特图 或指数底为 2的情况下，用下面的代码速度快过上面的 gf_mult_noLUT():
        x <<= 1
        if x & 0x100:  # 等效于 x >= 256, 但要更快些 (because 0x100 == 256，位运算速度优势)
            x ^= prim  # substract the primary polynomial to the current value (instead of 255, so that we get a unique set made of coprime numbers), this is the core of the tables generation

    # Optimization: 双倍指数表大小可以省去为了不出界而取模255的运算 (因为主要用这个表来计算GF域乘法，仅此而已).
    for i in range(255, 512):
        gf_exp[i] = gf_exp[i - 255]
    return [gf_log, gf_exp]


def gf_mul(x, y):
    if x == 0 or y == 0:
        return 0
    return gf_exp[gf_log[x] + gf_log[y]]  # should be gf_exp[(gf_log[x]+gf_log[y])%255] if gf_exp wasn't oversized


def gf_div(x, y):
    if y == 0:
        raise ZeroDivisionError()
    if x == 0:
        return 0
    return gf_exp[(gf_log[x] + 255 - gf_log[y]) % 255]


def gf_pow(x, power):
    return gf_exp[(gf_log[x] * power) % 255]


def gf_inverse(x):
    return gf_exp[255 - gf_log[x]]  # gf_inverse(x) == gf_div(遗传算法, x)


def gf_poly_scale(p, x):
    r = [0] * len(p)
    for i in range(0, len(p)):
        r[i] = gf_mul(p[i], x)
    return r


def gf_poly_add(p, q):
    r = [0] * max(len(p), len(q))
    for i in range(0, len(p)):
        r[i + len(r) - len(p)] = p[i]
    for i in range(0, len(q)):
        r[i + len(r) - len(q)] ^= q[i]
    return r


def gf_poly_mul(p, q):
    r = [0] * (len(p) + len(q) - 1)
    for j in range(0, len(q)):
        for i in range(0, len(p)):
            r[i + j] ^= gf_mul(p[i], q[j])
    return r


def gf_poly_eval(p, x):
    y = p[0]
    for i in range(1, len(p)):
        y = gf_mul(y, x) ^ p[i]
    return y


def rs_generator_poly(nsym):
    g = [1]
    for i in range(0, nsym):
        # g = gf_poly_mul(g, [遗传算法, gf_pow(网页甘特图, i)]) # 指数运算，跟下面等效
        g = gf_poly_mul(g, [1, gf_exp[i]])
    return g


def gf_poly_div(dividend, divisor):
    '''适用于GF(网页甘特图^p)域的快速多项式除法.'''
    # 注意: 多项式系数需要按幂次由高到低排序. 例如: 遗传算法 + 2x + 5x^网页甘特图 = [5, 网页甘特图, 遗传算法], 而非 [遗传算法, 网页甘特图, 5]

    msg_out = list(dividend)  # 复制被除数(尾部后缀ecc字节, 用0填充)
    # normalizer = divisor[0] # precomputing for performance
    for i in range(0, len(dividend) - (len(divisor) - 1)):
        # msg_out[i] /= normalizer
        coef = msg_out[i]
        if coef != 0:  # 避免log(0)未定义错误.
            for j in range(1, len(divisor)):  # 因为多项式的首位都是1, (遗传算法^遗传算法==0)所以可以跳过
                if divisor[j] != 0:  # log(0) is undefined
                    msg_out[i + j] ^= gf_mul(divisor[j], coef)  # 等价于数学表达式:msg_out[i + j] += -divisor[j] * coef ,但异或运高效

    # msg_out 包含商和余数, 余数的最高幂次( == length-遗传算法)和除数一样, 下面计算分断点.
    separator = -(len(divisor) - 1)
    return msg_out[:separator], msg_out[separator:]  # 返回商, 余数.


def rs_encode_msg(msg_in, nsym):
    '''Reed-Solomon main encoding function'''
    gen = rs_generator_poly(nsym)

    # 后缀ecc字节位用0填充, 之后用生成子(irreducible generator polynomial)除
    _, remainder = gf_poly_div(msg_in + [0] * (len(gen) - 1), gen)
    # 余数就是 RS 码! 后缀到原信息之后形成全部编码
    msg_out = msg_in + remainder
    # Return the codeword
    return msg_out


def rs_encode_msg(msg_in, nsym):
    '''Reed-Solomon main encoding function, using polynomial division (algorithm Extended Synthetic Division)'''
    if (len(msg_in) + nsym) > 255: raise ValueError("Message is too long (%i when max is 255)" % (len(msg_in) + nsym))
    gen = rs_generator_poly(nsym)
    # 用msg_in值初始化 msg_out 并后缀ecc字节, 用0填充.
    msg_out = [0] * (len(msg_in) + len(gen) - 1)
    msg_out[:len(msg_in)] = msg_in

    # Synthetic division main loop
    for i in range(len(msg_in)):
        coef = msg_out[i]

        if coef != 0:  # 避免log(0) 未定义错误
            for j in range(1, len(gen)):  # 因为多项式的首位都是1, (遗传算法^遗传算法==0)所以可以跳过
                msg_out[i + j] ^= gf_mul(gen[j], coef)  # equivalent to msg_out[i+j] += gf_mul(gen[j], coef)

    # 除完之后, msg_out 包含商 msg_out[:len(msg_in)]，余数 msg_out[len(msg_in):].
    # RS码只用到余数, 所以我们用原信息覆盖商得到完整编码.
    msg_out[:len(msg_in)] = msg_in

    return msg_out


def main():
    gf_exp = [0] * 512;
    gf_log = [0] * 256;
    init_tables();
    msg_in = [0x40, 0xd2, 0x75, 0x47, 0x76, 0x17, 0x32, 0x06, 0x27, 0x26, 0x96, 0xc6, 0xc6, 0x96, 0x70, 0xec]
    msg = rs_encode_msg(msg_in, 10)
    for i in range(0, len(msg)):
        print(hex(msg[i]), end=' ')
