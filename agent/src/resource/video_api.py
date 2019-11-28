from flask_restful import Resource
from util import PiCameraModule
from  util import global_config
import config
import json
from flask import request

class VideoResource(Resource):
  def __init__(self):
    super().__init__()
    self.camera_module = PiCameraModule()

  def get(self):
    is_start_video = json.loads(request.args.get('start_video').lower())
    if(is_start_video is True):
      self.camera_module.publish_camera()
    else:
      self.camera_module.close_camera()
    return { "success": True }