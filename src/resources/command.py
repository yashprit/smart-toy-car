from flask_restful import Resource

class CommandResource(Resource):
  """ Verbs relative to the users """
  
  @staticmethod
  def get():
    return {"user": "OK"}