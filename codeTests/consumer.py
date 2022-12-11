from redis import Redis
from dotenv import load_dotenv
import os
import json
import requests

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

result = r.blpop("jobs")
code_to_run = json.loads(result[1])
jobid_redis_status = f"jobs:codeExec:{code_to_run['request_id']}:status"
r.rpush(jobid_redis_status, "received")

# Execute code
r.rpush(jobid_redis_status, "executing")
post_url = "https://agent-python.fly.dev/execute"
data = code_to_run
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
request = requests.post(post_url, headers=headers, json=data)
print(request.content)
execution = json.loads(request.content)
result = execution['result']
returncode = result['returncode']
stdout = result['stdout']
stderr = result['stderr']


r.rpush(jobid_redis_status, "done")
jobid_redis_result = f"jobs:codeExec:{code_to_run['request_id']}:result"
r.rpush(jobid_redis_result, returncode, stdout, stderr)
