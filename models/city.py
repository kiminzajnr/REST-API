from db import db


class CityModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    state_id = db.Column(db.Integer, unique=False, nullable=False)