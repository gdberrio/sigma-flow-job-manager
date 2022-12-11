import os
from dotenv import load_dotenv
from redis import Redis
from rq import Queue, Worker, Connection

load_dotenv()
redis_pwd = os.getenv('REDIS_PWD')

r = Redis(
host= 'eu1-magical-dingo-38211.upstash.io',
port= '38211',
password= redis_pwd,
ssl=True
)

listen = ['default']

if __name__ == '__main__':
    with Connection(r):
        worker = Worker(list(map(Queue, listen)))
        worker.work()