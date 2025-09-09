import redis
import os

class Redis :
    def __init__(self):
        self.cli = redis.Redis(host=os.getenv("REDIS_HOST"),port=6379,db=0)

    def set_history(self):
        pass
    def Set(self):
        pass