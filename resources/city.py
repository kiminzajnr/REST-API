import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import cities

blp = Blueprint("Cities", __name__, description="Operations on items")

@blp.route("/city/<string:item_id")
class City(MethodView):
    def get_city(self, city_id):
        try:
            return cities[city_id]
        except KeyError:
            return {"message": "City not found"}, 404
        
    def delete_city(city_id):
        try:
            del cities[city_id]
            return {"message": "City deleted."}
        except KeyError:
            return {"message": "City not found"}, 404