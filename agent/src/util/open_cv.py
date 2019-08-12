import time
import sys
import cv2
import traceback
import config
from util import global_config
from .kafka_agent import KafkaAgent

producer = KafkaAgent(config.KAFKA_BROKERS, config.TOPIC)

def publish_camera(brokers, topic):
  print(type(global_config.start_video))
  if(global_config.start_video == True):
    camera = cv2.VideoCapture(0)
    try:
      while(True):
        success, frame = camera.read()
        ret, jpeg = cv2.imencode('.png', frame)
        producer.send_data(jpeg.tobytes())
        time.sleep(0.2)

    except cv2.error as e:
      print(e)
      camera.release()
      sys.exit(1)
  else:
    print(global_config.start_video)
    camera = cv2.VideoCapture(0)
    camera.release()