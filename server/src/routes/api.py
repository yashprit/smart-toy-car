from flask import Blueprint
from flask_restful import Api
from resources import ApiResource

API_BLUEPRINT = Blueprint("api", __name__)
Api(API_BLUEPRINT).add_resource(ApiResource, "/")