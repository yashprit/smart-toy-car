from flask_restful import Resource, request
from util import gpio_process

class CommandResource(Resource):
  def get(self):
    type = request.args.get('type')
    gpio_process(type)
    return {"type": type}