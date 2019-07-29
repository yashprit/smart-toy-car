from flask_restful import Resource
from util import open_cv
from  util import global_config
import config
from flask import request

class VideoResource(Resource):
  def get(self):
    global_config.start_video = request.args.get('start_video') 
    print(global_config.start_video, request.args.get('start_video'))
    open_cv.publish_camera(config.KAFKA_BROKERS, config.TOPIC)
    print("video api")
    return {"status": True}