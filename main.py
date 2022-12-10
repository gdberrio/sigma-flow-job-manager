import redis

import redis

r = redis.Redis(
  host= 'eu1-magical-dingo-38211.upstash.io',
  port= '38211',
  password= '********',
  ssl=True
)

r.set('foo','bar')
print(r.get('foo'))