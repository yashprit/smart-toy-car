import time
import base64
import picamera
from util import global_config
from .kafka_agent import KafkaAgent

producer = KafkaAgent(config.KAFKA_BROKERS, config.TOPIC)

class PiCameraModule:
  picam = ''

  def __init__(self):
    super().__init__()
    self.picam = picamera.PiCamera()
    self.picam.resolution = (640, 480)

  def publish_camera(self):
    print(type(global_config.start_video))
    output = StringIO.StringIO()
    while True:
      output.seek(0)
      self.picam.capture(output, format="jpeg", use_video_port=True)
      encoded_string = base64.b64encode(output.getvalue())
      producer.send_data({"image": encoded_string})
      time.sleep(0.16)
      output.flush()
  
  def close_camera(self):
    self.picam.close()