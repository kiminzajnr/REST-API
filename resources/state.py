import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StateSchema
from db import states


blp = Blueprint("states", __name__, description="Operations on states")

@blp.route("/state/<string:state_id>")
class State(MethodView):
    @blp.response(200, StateSchema)
    def get(cls, state_id):
        try:
            return states[state_id]
        except KeyError:
            abort(404, message="State not found")
    
    def delete(cls, state_id):
        try:
            del states[state_id]
            return {"message": "State deleted."}
        except KeyError:
            abort(404, message="State not found.")
        
@blp.route("/state")
class StateList(MethodView):
    @blp.response(200, StateSchema(many=True))
    def get(cls):
        return states.values()
    
    @blp.arguments(StateSchema)
    @blp.response(201, StateSchema)
    def post(cls, state_data):
        for state in states.values():
            if state_data["name"] == state["name"]:
                abort(400, message=f"State already exists.")

        state_id = uuid.uuid4().hex
        state = {**state_data, "id": state_id}
        states[state_id] = state

        return state
