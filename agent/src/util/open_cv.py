import time
import sys
import cv2
from util import global_config
from .kafka_agent import KafkaAgent

def publish_camera(brokers, topic):
  print(global_config.start_video)
  if(global_config.start_video):
    producer = KafkaAgent(brokers, topic)
    camera = cv2.captureVideo(0)
    try:
      while(True):
        success, frame = video.read()
        ret, buffer = cv2.imencode('.jpg', frame)
        producer.send_data(buffer.tobytes())
        time.sleep(0.2)

    except:
      print("Existing")
      sys.exit(1)

    camera.release()
