import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StateSchema
from db import states


blp = Blueprint("states", __name__, description="Operations on states")

@blp.route("/state/<string:state_id>")
class State(MethodView):
    def get(self, state_id):
        try:
            return states[state_id]
        except KeyError:
            return {"message": "State not found"}, 404  
    
    def delete(self, state_id):
        try:
            del states[state_id]
            return {"message": "State deleted."}
        except KeyError:
            return {"message": "State not found."}, 404
        
@blp.route("/state")
class StateList(MethodView):
    def get(self):
        return {"states": list(states.values())}
    
    @blp.arguments(StateSchema)
    def post(self, state_data):
        for state in states.values():
            if state_data["name"] == state["name"]:
                abort(400, message=f"Store already exists.")

        state_id = uuid.uuid4().hex
        state = {**state_data, "id": state_id}
        states[state_id] = state

        return state
