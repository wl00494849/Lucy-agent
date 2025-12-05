import redis
import os

class Redis :
    def __init__(self):
        self.cli = redis.Redis(host=os.getenv("REDIS_HOST"),port=6379,db=0)

    def simple_short_memory(memory:str):
        pass
    
    def get_memory(userid:str)->str:
        pass