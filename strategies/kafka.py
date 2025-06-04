from .interface import OutputStrategy
from kafka import KafkaProducer
import json


class KafkaStrategy(OutputStrategy):
    def __init__(self, bootstrap_servers='localhost:9092', topic='police_incidents'):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def output(self, data: list[dict]):
        for item in data:
            self.producer.send(self.topic, item)
        self.producer.flush()
