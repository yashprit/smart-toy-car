from flask import Flask, Response, request
from kafka import KafkaConsumer
import config
import requests

server = Flask(__name__)

server.debug = config.DEBUG

consumer = KafkaConsumer(config.TOPIC, bootstrap_servers = config.KAFKA_BROKERS)

@server.route('/api', methods=['GET'])
def api():
  return "API's are working"

@server.route('/command', methods=['GET'])
def command():
  type = request.args.get('type')
  result = requests.get(config.CLIENT + "/command?type=" + type)
  return result.json()

@server.route('/video-stream', methods=['GET'])
def video_steam():
  status = request.args.get('status')
  result = requests.get(config.CLIENT + "/video?start_video=" + status)
  return result.json()

@server.route('/video', methods=['GET'])
def video():
  return Response(
      get_video_stream(), 
      mimetype='multipart/x-mixed-replace; boundary=frame')

def get_video_stream():
  for msg in consumer:
      yield (b'--frame\r\n'
              b'Content-Type: image/jpg\r\n\r\n' + msg.value + b'\r\n\r\n')


if __name__ == "__main__":
  server.run(host=config.HOST, port=config.PORT)