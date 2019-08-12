from flask import Flask, Response, request
from kafka import KafkaConsumer
import config
import requests
from flask_socketio import SocketIO, emit

server = Flask(__name__)
server.debug = config.DEBUG
server

socketio = SocketIO(server)

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

@socketio.on('video', namespace='/test')
def video():
  for msg in consumer:
    emit('frame', {'data': msg.value}, broadcast=True)

if __name__ == "__main__":
  socketio.run(server, host=config.HOST, port=config.PORT)