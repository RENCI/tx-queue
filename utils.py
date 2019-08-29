import redis
from rq import Queue, Worker
import os

def redisQueue():
    return redis.StrictRedis(host=os.environ["REDIS_QUEUE_HOST"], port=int(os.environ["REDIS_QUEUE_PORT"]), db=int(os.environ["REDIS_QUEUE_DB"]))


def startWorker():
    conn = redisQueue()
    worker = Worker(Queue(connection=conn), connection=conn)
    worker.work()

    
