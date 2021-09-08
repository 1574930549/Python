from redis.sentinel import Sentinel
from redis import WatchError
MYSETINEL = None
MASTER = None
SLAVE = None

# 1.redis 哨兵模式集群最少需要一主三从, 三哨兵
# 2.redis 哨兵集群所有主从节点都完整的保存了一份数据
SENTINEADDRESS = [
    ('121.89.197.4', 26379),
    ('39.101.133.206', 26380),
    # ('81.70.135.23', 26381),
]


def get_redis_conn():

    global MYSETINEL
    global MASTER
    global SLAVE
# 如果哨兵连接实例已存在, 不重复连接, 当连接失效时, 重新连接
    if not MYSETINEL:# 连接哨兵
        MYSETINEL = Sentinel(SENTINEADDRESS, socket_timeout=2000)  # 尝试连接最长时间单位毫秒, 1000毫秒为1秒
        # 通过哨兵获取主数据库连接实例      参数1: 主数据库的名字(集群部署时在配置文件里指明)
        MASTER = MYSETINEL.master_for('mymaster', socket_timeout=2000)
        # 通过哨兵获取从数据库连接实例    参数1: 从数据的名字(集群部署时在配置文件里指明)
        SLAVE = MYSETINEL.slave_for('mymaster', socket_timeout=2000)
        print(MASTER)
        print(SLAVE)
        master = MYSETINEL.discover_master('mymaster')
        print(master)
        slave = MYSETINEL.discover_slaves('mymaster')
        print(slave)



# 往 主数据库 写入数据
def setcache(key, time, value):
    global MASTER
    if MASTER:
        return MASTER.setex(key, time, value)
    else:
        return False


# 从 从数据库 读取数据
def getcache(key):
    global SLAVE
    if SLAVE:
        return SLAVE.get(key)
    else:
        return False


# 每次都先尝试生成连接实例
if __name__=="__main__":
    get_redis_conn()