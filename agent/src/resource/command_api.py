from flask_restful import Resource, request
from util import CommandControl

commandControl = CommandControl();

class CommandResource(Resource):
  def get(self):
    type = request.args.get('type')
    commandControl.gpio_process(type)
    return {"type": type}