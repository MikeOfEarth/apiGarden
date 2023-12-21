from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Str(dump_only = True)
    username = fields.Str(required = True)
    name = fields.Str()
    email = fields.Str(required = True)    
    password = fields.Str(required = True, load_only = True )

class CropSchema(Schema):
    crop_name = fields.Str(required = True)
    seasons = fields.List(required=True)
    light_preference = fields.Str(required=True)
    grow_time = fields.Int(required=True)
    companions = fields.List(required=True)
    count_per_harvest = fields.Int(required=True)
    repeat_harvest = fields.Int(required=True)

class PlotSchema(Schema):
    grid_id = fields.Str(required=True)
    owner = fields.Str(required = True)
    light = fields.Str(required = True)
    crop = fields.Str()
    time = fields.DateTime(dump_only = True)
    watered = fields.Bool(required = True)
    tilled = fields.Bool(required = True)
    fertilizer = fields.Bool(required = True)
