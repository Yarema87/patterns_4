from .interface import OutputStrategy
import redis
import json


class RedisStrategy(OutputStrategy):
    def __init__(self, host='localhost', port=6379, db=0, channel='police_incidents'):
        self.client = redis.Redis(host=host, port=port, db=db)
        self.channel = channel

    def output(self, data: list[dict]):
        message = json.dumps(data)
        self.client.publish(self.channel, message)

