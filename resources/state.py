import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StateSchema

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import StateModel


blp = Blueprint("states", __name__, description="Operations on states")

@blp.route("/state/<string:state_id>")
class State(MethodView):
    @blp.response(200, StateSchema)
    def get(cls, state_id):
        state = StateModel.query.get_or_404(state_id)
        return state
    
    def delete(self, state_id):
        state = StateModel.query.get_or_404(state_id)
        db.session.delete(state)
        db.session.commit()
        return {"message": "State deleted"}, 200
        
@blp.route("/state")
class StateList(MethodView):
    @blp.response(200, StateSchema(many=True))
    def get(self):
        return StateModel.query.all()
    
    @blp.arguments(StateSchema)
    @blp.response(201, StateSchema)
    def post(self, state_data):
        state = StateModel(**state_data)

        try:
            db.session.add(state)
            db.session.commit()
        except IntegrityError:
            abort(
            400,
            message="A state with that name already exists.",
        )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the state.")

        return state
