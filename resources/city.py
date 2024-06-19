import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required

from schemas import CitySchema, CityUpdateSchema

from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import CityModel

blp = Blueprint("Cities", __name__, description="Operations on cities")

@blp.route("/city/<string:city_id>")
class City(MethodView):
    @blp.response(200, CitySchema)
    def get(self, city_id):
        city = CityModel.query.get_or_404(city_id)
        return city
        
    @jwt_required()
    def delete(self, city_id):
        city = CityModel.query.get_or_404(city_id)
        db.session.delete(city)
        db.session.commit()
        return {"message": "City deleted."}
    
    @blp.arguments(CityUpdateSchema)
    @blp.response(200, CitySchema)
    def put(self, city_data, city_id):
        city = CityModel.query.get_or_404(city_id)
        if city:
            city.name = city_data["name"]
        else:
            city = CityModel(id=city_id, **city_data)

        db.session.add(city)
        db.session.commit()

        return city
        
@blp.route("/city")
class CityList(MethodView):
    @blp.response(200, CitySchema(many=True))
    def get(self):
        return CityModel.query.all()
    
    @blp.arguments(CitySchema)
    @blp.response(201, CitySchema)
    def post(self, city_data):
        city = CityModel(**city_data)

        try:
            db.session.add(city)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the city.")

        return city