import uuid
from flask import Flask, request
from db import states, cities


app = Flask(__name__)


@app.get("/state")
def get_states():
    return {"states": list(states.values())}

@app.get("/city")
def get_cities():
    return {"cities": list(cities.values())}

@app.post("/state")
def create_state():
    state_data = request.get_json()
    state_id = uuid.uuid4().hex
    state = {**state_data, "id": state_id}
    states[state_id] = state

    return state

@app.post("/state/<string:name>/city")
def create_city(name):
    city_data = request.get_json()
    if city_data["state_id"] not in states:
        return {"message": "State not found"}, 404
    city_id = uuid.uuid4().hex
    city = {**city_data, "id": city_id}

    return city

@app.get("/state/<string:name>")
def get_state(state_id):
    try:
        return states[state_id]
    except KeyError:
        return {"message": "State not found"}, 404

@app.get("/city/<string:city_id>")
def get_city(city_id):
    try:
        return cities[city_id]
    except KeyError:
        return {"message": "City not found"}, 404