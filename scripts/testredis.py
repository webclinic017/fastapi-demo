import json
import base64
from redis import StrictRedis

CACHE_REDIS_HOST =  '127.0.0.1'
CACHE_REDIS_PORT =  63790
CACHE_REDIS_DB = '1'
CACHE_REDIS_PASSWORD =  'greenvalley'

# 'redis://auth:password@redishost:6379/0'
CELERY_BROKER_URL = 'redis://auth:%s@%s:%s/12' % (CACHE_REDIS_PASSWORD, CACHE_REDIS_HOST, CACHE_REDIS_PORT,)

CELERY_RESULT_BACKEND = 'redis://auth:%s@%s:%s/13' % (CACHE_REDIS_PASSWORD, CACHE_REDIS_HOST, CACHE_REDIS_PORT,)
print(CELERY_RESULT_BACKEND)



redis_client = StrictRedis.from_url(CELERY_RESULT_BACKEND)




#适合数据量小的时候
tasks = redis_client.keys('celery-task*')
task0 = redis_client.keys('celery-task*')[0]
rs = redis_client.get(task0)


#get all counts
from itertools import zip_longest
# iterate a list in batches of size n
def batcher(iterable, n):
    args = [iter(iterable)] * n
    return zip_longest(*args)

# in batches of 500 delete keys matching user:*
counter=0
for keybatch in batcher(redis_client.scan_iter('celery-task*'),500):
    print(*keybatch)
    for key in keybatch:
        if key != None:
            counter += 1
print(counter)

cursor, keys = redis_client.scan(match='celery-task*')
data = redis_client.mget(keys)

print(data)
    #r.delete(*keybatch)




#print({json.loads(base64.b64decode(json.loads(message.decode('utf-8'))['body']).decode('utf-8'))['task'] for message in default_queue})