
from redis.sentinel import Sentinel

sentinel_list = [('121.89.197.4', 26379),
                 ('39.101.133.206', 26380),
                 ('81.70.135.23', 26381),
                 ]
mySentinel = Sentinel(sentinel_list, 123)
master = mySentinel.master_for("mymaster", db=0)
slave = mySentinel.slave_for("mymaster", db=0)

# 使用master进行写的操作，使用slave进行读的操作
master.hset("key_name", "filed", "value")
slave.hget("key_name", "filed")
slave.hgetall("key_name")
