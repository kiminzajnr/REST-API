# RESTful-Flask-API
Endpoints to manage states and cities.
create, read, update, and delete states and cities.

# Endpoints
- `GET /state` - Retrieve a list of all states.
- `POST /state` - Create a new state.
- `GET /state/<string:state_id>` - Retrieve a state given its ID.
- `DELETE /state/<string:state_id>` - Delete a state given its ID.
- `GET /city` - Retrieve a list of all cities.
- `POST /city` - Create a new city.
- `GET /city/<string:city_id>` - Retrieve a city given its ID.
- `PUT /city/<string:city_id>` - Update a city given its ID.
- `DELETE /city/<string:city_id>` - Delete a city given its ID.

# Setup

## Using virtual env
```
git clone https://github.com/kiminzajnr/RESTful-Flask-API.git
cd RESTful-Flask-API
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

#### Run the app
```
flask run
```

## Using docker
```
git clone https://github.com/kiminzajnr/RESTful-Flask-API.git
cd RESTful-Flask-API
docker build -t flask-api .
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-api
```

#### Common error when using docker
`Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:5000 -> 0.0.0.0:0: listen tcp 0.0.0.0:5000: bind: address already in use.`

#### Fix
- Use another port:
    - `docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-api`
- Or, kill process running on the port if not needed:
    - Run `lsof -i :5000` and note the `PID`
    - Run `kill -9 PID` - `PID` obtained from above

`docker: Cannot connect to the Docker daemon at ... docker.sock. Is the docker daemon running?.`
