from kafka import KafkaProducer
import json
import config

class KafkaAgent(object):
  
  def __init__(self, topic):
    self.topic = config.TOPIC
    self.produce = KafkaProducer(bootstrap_servers = config.KAFKA_BROKERS)

  def send_data(self, json_data):
    self.produce.send(self.topic, json_data)