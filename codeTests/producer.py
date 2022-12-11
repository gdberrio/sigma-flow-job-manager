from redis import Redis
from dotenv import load_dotenv
import os
import json

load_dotenv()
redis_pwd = os.getenv('REDIS_PWD')

r = Redis(
host= 'eu1-magical-dingo-38211.upstash.io',
port= '38211',
password= redis_pwd,
ssl=True,
charset="utf-8",
decode_responses=True
) # type: ignore

code_1 = {
    "request_id" : 3,
    "code": "print(\"hello code 3\")"
    }

code_1_serialized = json.dumps(code_1)
r.rpush("jobs", code_1_serialized)

code_1 = {
    "request_id" : 4,
    "code": "print(\"hello code 4\")"
    }

code_1_serialized = json.dumps(code_1)
r.rpush("jobs", code_1_serialized)