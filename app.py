from flask import Flask

app = Flask(__name__)

states = [
    {
        "name": "Alabama", "cities": [{"name": "Birmingham"}, {"name": "Montgomery"}, {"name": "Mobile"}]
    }
]

@app.get("/state")
def get_states():
    return {"states": states}