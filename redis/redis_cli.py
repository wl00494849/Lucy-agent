import redis
import os

class Redis :
    def __init__(self):
        self.cli = redis.Redis(host=os.getenv("REDIS_HOST"),port=6379,db=0)

    def push_list(self,uid:str,message:str):
        key = f"list:{uid}"
        exist = self.cli.exists(key)
        self.cli.lpush(key,message,)
        if not exist:
            self.cli.expire(key,1800)

    def Set(self):
        pass