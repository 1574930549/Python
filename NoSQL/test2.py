# AIRFLOW__CELERY__BROKER_URL =" sentinel：// $ SENTINEL_HOST：$ SENTINEL_PORT"
# AIRFLOW__CELERY_BROKER_TRANSPORT_OPTIONS = {'master_name':"mymaster"}
from redis.sentinel import Sentinel
sentinel = Sentinel([
    ('121.89.197.4', 26379),
    ('39.101.133.206', 26380),
    ('81.70.135.23', 26381),
    ('124.71.184.227', 26382),
], socket_timeout=3000)
service_name = 'mymaster'

master = sentinel.discover_master('mymaster')
print(master)
slave = sentinel.discover_slaves('mymaster')
print(slave)

