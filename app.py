from flask import Flask, request

app = Flask(__name__)

states = [
    {
        "name": "Alabama", "cities": [{"name": "Birmingham"}, {"name": "Montgomery"}, {"name": "Mobile"}]
    }
]

@app.get("/state")
def get_states():
    return {"states": states}

@app.post("/state")
def create_state():
    request_data = request.get_json()
    new_state = {"name": request_data["name"], "cities": []}
    states.append(new_state)

    return new_state, 201

@app.post("/state/<string:name>/city")
def create_city(name):
    request_data = request.get_json()
    for state in states:
        if state["name"] == name:
            new_city = {"name": request_data["name"]}
            state["cities"].append(new_city)
            return new_city
    return {"message": "State not found"}, 404