# -*- coding: UTF-8 -*-

from rediscluster import RedisCluster

# 构建所有的节点
startup_nodes = [
    {"host": "121.89.197.4", "port": 6379, "password": "123"},
    {"host": "39.101.133.206", "port": 6380, "password": "123"},
    {"host": "81.70.135.23", "port": 6381, "password": "123"},
    {"host": "121.89.197.4", "port": 26379, "password": "123"},
    {"host": "39.101.133.206", "port": 26380, "password": "123"},
    {"host": "81.70.135.23", "port": 26381, "password": "123"},
]
# 构建StrictRedisCluster对象
redis_store = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
print(redis_store)
# redis_store.set("name", "helloworld")
# print("My name is: ", redis_store.get('name'))
