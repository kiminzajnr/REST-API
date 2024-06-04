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

@app.post("/city")
def create_city():
    city_data = request.get_json()
    if city_data["id"] not in states:
        return {"message": "State not found"}, 404
    city_id = uuid.uuid4().hex
    city = {**city_data, "id": city_id}
    cities[city_id] = city

    return city

@app.get("/state/<string:state_id>")
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
    
@app.delete("/city/<string:city_id>")
def delete_city(city_id):
    try:
        del cities[city_id]
        return {"message": "City deleted."}
    except KeyError:
        return {"message": "City not found"}, 404
    
@app.put("/city/<string:city_id>")
def update_city(city_id):
    city_data = request.get_json()
    try:
        city = cities[city_id]
        city |= city_data
        return city
    except KeyError:
        return {"message": "City not found."}, 404
    
@app.delete("/state/<string:state_id>")
def delete_state(state_id):
    try:
        del states[state_id]
        return {"message": "State deleted."}
    except KeyError:
        return {"message": "State not found."}, 404