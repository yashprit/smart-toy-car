from kafka import KafkaProducer
import json

class KafkaAgent(object):
  
  def __init__(self, kafka_broker, topic):
    self.topic = topic
    self.produce = KafkaProducer(
      value_serializer = lambda v: json.dumps(v).encode('utf-8'),
      bootstrap_servers = kafka_broker
    )

  def send_data(self, json_data):
    self.produce.send(self.topic, json_data)