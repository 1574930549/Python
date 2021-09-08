import redis
from redis import WatchError
from redis.sentinel import Sentinel
from redis import WatchError

MYSETINEL = None
MASTER = None
SLAVE = None

SENTINEADDRESS = [('121.89.197.4', 26379), ('39.101.133.206', 26380), ('81.70.135.23', 26381)]
# SENTINEADDRESS = [('121.89.197.4', 6379), ('39.101.133.206', 6380), ('81.70.135.23', 6381)]
# SENTINEADDRESS = [('121.89.197.4', 26379,123), ('39.101.133.206', 26320,123), ('81.70.135.23', 26381,123)]


# 选择要连接的数据库，默认是连接redis的 1 数据库
def get_redis_conn(db=0):
    global MYSETINEL
    global MASTER
    global SLAVE
    # 如果哨兵连接实例已存在, 不重复连接, 当连接失效时, 重新连接
    if not MYSETINEL:  # 连接哨兵
        MYSETINEL = Sentinel(SENTINEADDRESS,123)
        # 通过哨兵获取主数据库连接实例      参数1: 主数据库的名字(集群部署时在配置文件里指明)
        MASTER = MYSETINEL.master_for('mymaster')
        # 通过哨兵获取从数据库连接实例    参数1: 从数据的名字(集群部署时在配置文件里指明)
        SLAVE = MYSETINEL.slave_for('mymaster')


# 每次都先尝试生成连接实例
get_redis_conn()


# 使用哈希,往 主数据库 追加写入
def hAppendValue(name, key, value):
    global MASTER
    if MASTER:
        if MASTER.hexists(name, key):
            MASTER.hset(name, key, hGet(name, key) + value)
        else:
            MASTER.hset(name, key, value)
    else:
        return False


# 往 主数据库 追加写入
def appendValue(key, value):
    global MASTER
    if MASTER:
        if MASTER.exists(key):
            MASTER.append(key, value)
        else:
            MASTER.set(key, value)
    else:
        return False


# 往 主数据库 写入带有过期时间的数据
def setWithExpiresTime(key, value, expiresTime):
    global MASTER
    if MASTER:
        return MASTER.setex(key, expiresTime, value)
    else:
        return False


# 往 主数据库 写入的数据
def set(key, value):
    global MASTER
    if MASTER:
        return MASTER.set(key, value)
    else:
        return False


# 使用哈希, 往 主数据库 写入的数据
def hSet(name, key, value):
    global MASTER
    if MASTER:
        return MASTER.hset(name, key, value)
    else:
        return False


# 使用管道，哈希 往 主数据库 写入的数据
def hSetWithPipeLine(name, key, value):
    global MASTER
    if MASTER:
        with MASTER.pipeline() as pipe:
            pipe.hset(name, key, value)
            result = pipe.execute()
            return True, result
    else:
        return False


# 通过 主数据库 删除数据
def delete(key):
    global MASTER
    if MASTER:
        return MASTER.delete(key)
    else:
        return False


# 使用哈希， 通过 主数据库 删除数据
def hDelete(name, key):
    global MASTER
    if MASTER:
        return MASTER.hdel(name, key)
    else:
        return False


# 使用正则表达式，通过 主数据库 批量删除数据
def deleteWithPatten(Patten):
    global MASTER
    if MASTER:
        return MASTER.delete(*MASTER.keys(Patten))
    else:
        return False


# 清空所有数据
def flushDB():
    global MASTER
    if MASTER:
        return MASTER.flushdb()
    else:
        return False


# 通过 从数据库 读取数据
def get(key):
    global MASTER
    global SLAVE
    if SLAVE:
        result = SLAVE.get(key)
        return result.decode('UTF-8') if (str(type(result)) == "<class 'bytes'>" and len(result) > 0) else result
    else:
        if MASTER:
            result = MASTER.get(key)
            return result.decode('UTF-8') if (str(type(result)) == "<class 'bytes'>" and len(result) > 0) else result
        else:
            return False


# 使用哈希， 通过 从数据库 读取数据
def hGet(name, key):
    global MASTER
    global SLAVE
    if SLAVE:
        result = SLAVE.hget(name, key)
        return result.decode('UTF-8') if (str(type(result)) == "<class 'bytes'>" and len(result) > 0) else result
    else:
        if MASTER:
            result = MASTER.hget(name, key)
            return result.decode('UTF-8') if (str(type(result)) == "<class 'bytes'>" and len(result) > 0) else result
        else:
            return False


# 在并发,数据可能冲突的情况下，修改value
def alter(key, value):
    global MASTER
    with MASTER.pipeline() as pipe:
        i = 0
        while i < 10:  # 尝试修改库存10次
            try:
                # watch库存键, multi后如果该key被其他客户端改变, 事务操作会抛出WatchError异常
                pipe.watch(key)
                pipe.set(key, value)  # 保存剩余库存
                # 事务结束, 把命令推送过去
                result = pipe.execute()  # execute返回命令执行结果列表,
                return True, result
            except WatchError as e:
                print(e)
                i += 1
                continue
            finally:
                pipe.reset()

#
# get_redis_conn()
# hSetWithPipeLine("test", "kzx11132", ":sad")
#
set( "kzx11132", ":sad")
print(get("kzx11132"))
