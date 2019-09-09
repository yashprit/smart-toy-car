from flask import Flask, Response, request
from kafka import KafkaConsumer
import config
import requests
from flask_socketio import SocketIO, emit

server = Flask(__name__)
server.debug = config.DEBUG

socketio = SocketIO(server, cors_allowed_origins="*")

consumer = KafkaConsumer(bootstrap_servers=config.KAFKA_BROKERS, auto_offset_reset='latest')

print(consumer)

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

@socketio.on('video', namespace='/video')
def video():
  print("video")
  consumer.subscribe(topics=config.TOPIC)
  for msg in consumer:
    print(msg.value)
    emit('frame', {'data': msg.value}, broadcast=True)

if __name__ == "__main__":
  socketio.run(server, host=config.HOST, port=config.PORT)