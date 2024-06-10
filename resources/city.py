import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import CitySchema, CityUpdateSchema
from db import cities

blp = Blueprint("Cities", __name__, description="Operations on cities")

@blp.route("/city/<string:city_id>")
class City(MethodView):
    @blp.response(200, CitySchema)
    def get(self, city_id):
        try:
            return cities[city_id]
        except KeyError:
            return abort(404, message="City not found")
        
    def delete(city_id):
        try:
            del cities[city_id]
            return {"message": "City deleted."}
        except KeyError:
            return abort(404, message="City not found")
    
    @blp.arguments(CityUpdateSchema)
    @blp.response(200, CitySchema)
    def put(self, city_data, city_id):
        try:
            city = cities[city_id]
            city |= city_data
            return city
        except KeyError:
            abort(404, message="City not found.")
        
@blp.route("/city")
class CityList(MethodView):
    @blp.response(200, CitySchema(many=True))
    def get(self):
        return cities.values()
    
    @blp.arguments(CitySchema)
    @blp.response(201, CitySchema)
    def post(self, city_data):
        for city in cities.values():
            if (
                city_data["name"] == city["name"]
                and city["state_id"] == city["state_id"]
            ):
                abort(404, message=f"City already exists.")

        city_id = uuid.uuid4().hex
        city = {**city_data, "id": city_id}
        cities[city_id] = city

        return city