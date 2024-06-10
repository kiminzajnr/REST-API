import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
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
