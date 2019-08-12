from flask_restful import Resource
from util import open_cv
from  util import global_config
import config
import json
from flask import request

class VideoResource(Resource):
  def get(self):

    global_config.start_video = json.loads(request.args.get('start_video').lower())
    open_cv.publish_camera(config.KAFKA_BROKERS, config.TOPIC)
    return {"status": True}