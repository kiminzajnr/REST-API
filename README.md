# Know-US States REST API
A complete REST API built with Flask and Python

![API Screenshot](/sc.png)

# API Endpoints

## Users

| Method | Endpoint          | Description                                       |
|--------|-------------------|---------------------------------------------------|
| POST   | /register         | Create user accounts given an email and password. |
| POST   | /login            | Get a JWT given an email and password.            |
| 🔒 POST | /logout          | Revoke a JWT.                                     |
| 🔒 POST | /refresh          | Get a fresh JWT given a refresh JWT.              |
| GET    | /user/{user_id}   | (dev-only) Get info about a user given their ID.  |
| DELETE | /user/{user_id}   | (dev-only) Delete a user given their ID.          |

## States

| Method | Endpoint          | Description                                       |
|--------|-------------------|---------------------------------------------------|
| POST   | /state            | Create a state given a its name.                  |
| GET   | /state             | Get a list of states.                             |
| GET | /state/{state_id}    | Delete a state given its ID.                      |
| DELETE | /state/{state_id} | Get a state given its ID.                         |

## Cities

| Method | Endpoint          | Description                                       |
|--------|-------------------|---------------------------------------------------|
| POST   | /city             | Create a city given its name and state ID.        |
| GET    | /city             | Get a list of cities.                             |
| GET    | /city/{city_id}   | Get a city given its ID.                          |
| PUT    | /city/{city_id}   | Update a city given its ID.                       |
| DELETE | /city/{user_id}   | Delete a city given its ID.                       |

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

#### Common errors when using docker
`Error response from daemon: Ports are not available: exposing port TCP 0.0.0.0:5000 -> 0.0.0.0:0: listen tcp 0.0.0.0:5000: bind: address already in use.`

- Use another port:
    - `docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-api`
- Or, kill process running on the port if not needed:
    - Run `lsof -i :5000` and note the `PID`
    - Run `kill -9 PID` - `PID` obtained from above

`docker: Cannot connect to the Docker daemon at ... docker.sock. Is the docker daemon running?.`
- If on macOS/Windows run docker desktop.
- On Linux start docker service.


# Usage

![Usage Video](/output.gif)

# License
[MIT license](/LICENSE)
