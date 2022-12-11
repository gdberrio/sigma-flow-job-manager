from redis import Redis
from datetime import datetime, timedelta
from rq import Queue
from dotenv import load_dotenv
import os
import task

load_dotenv()
redis_pwd = os.getenv('REDIS_PWD')

r = Redis(
host= 'eu1-magical-dingo-38211.upstash.io',
port= '38211',
password= redis_pwd,
ssl=True,
charset="utf-8",
decode_responses=True
)

queue = Queue(connection=r)

def queue_tasks():
    queue.enqueue(task.print_task, 5)
    queue.enqueue_in(timedelta(seconds=10), task.print_numbers, 5)

def main():
    queue_tasks()

if __name__ == "__main__":
    main()