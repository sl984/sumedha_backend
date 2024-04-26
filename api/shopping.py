import json, jwt
from flask import Blueprint, request, jsonify, current_app, Response
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime
from auth_middleware import token_required

from model.shopping_model import ShoppingModel

shopping_api = Blueprint('shopping_api', __name__,
                        url_prefix='/api/shopping')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(shopping_api)

class Predict(Resource):
    def post(self):
        data = request.json
        shopping_model = ShoppingModel.get_instance()
        result = shopping_model.predict(data)
        #return {'message': 'Predict resource', 'total_price': result}

api.add_resource(Predict, '/predict')