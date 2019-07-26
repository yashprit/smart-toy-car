from flask_restful import Resource

class ApiResource(Resource):
  """ Verbs relative to the users """
  def get(self):
    return "API's are working"