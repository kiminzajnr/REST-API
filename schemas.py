from marshmallow import Schema, fields

class PlainCitySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class PlainStateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class CitySchema(PlainCitySchema):
    state_id = fields.Int(required=True, load_only=True)
    state = fields.Nested(PlainStateSchema(), dump_only=True)


class CityUpdateSchema(Schema):
    name = fields.Str()
    state_id = fields.Int()


class StateSchema(PlainStateSchema):
    cities = fields.List(fields.Nested(PlainStateSchema()), dump_only=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class UserRegsterSchema(UserSchema):
    email = fields.Str(required=True)