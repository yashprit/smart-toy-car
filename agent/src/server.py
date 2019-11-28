from flask import Flask
from flask_restful import Api
#from resource import VideoResource
from resource import CommandResource
import config

server = Flask(__name__)
api = Api(server)
api.add_resource(CommandResource, "/command")
api.add_resource(VideoResource, "/video")

server.debug = config.DEBUG

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT)