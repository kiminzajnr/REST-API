from db import db


class CityModel(db.Model):
    __tablename__ = "cities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    state_id = db.Column(
        db.Integer, db.ForeignKey("states.id"), unique=False, nullable=False
    )
    state = db.relationship("StateModel", back_populates="cities")