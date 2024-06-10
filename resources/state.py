import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import states


blp = Blueprint("states", __name__, description="Operations on states")

@blp.route("/state/<string:state_id")
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
    
    def post(self):
        state_data = request.get_json()
        if "name" not in state_data:
            abort(
                400,
                message="Bad request. Ensure 'name' is included in JSON payload."
            )
        for state in states.values():
            if state_data["name"] == state["name"]:
                abort(400, message=f"Store already exists.")

        state_id = uuid.uuid4().hex
        state = {**state_data, "id": state_id}
        states[state_id] = state

        return state
