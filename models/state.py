from db import db


class StateModel(db.Model):
    __tablename__ = "states"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    cities = db.relationship("CityModel", back_populates="state", lazy="dynamic")