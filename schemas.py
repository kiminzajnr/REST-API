from marshmallow import Schema, fields


class CityScema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    state_id = fields.Str(required=True)


class CityUpdateSchema(Schema):
    name = fields.Str()


class StateSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
