from flask import Blueprint
from flask_restful import Api
from resources import CommandResource

COMMAND_BLUEPRINT = Blueprint("command", __name__)
Api(COMMAND_BLUEPRINT).add_resource(CommandResource, "/command")