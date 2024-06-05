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
```