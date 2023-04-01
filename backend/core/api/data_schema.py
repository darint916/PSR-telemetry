from cerberus import Validator

battery_schema = {
    'time': {'type': 'integer', 'required': True},
    'activated': {'type': 'boolean', 'required': True},
    'percent': {'type': 'integer', 'required': True},
    'units': {'type': 'string', 'required': True},
    'battery_health': {'type': 'string', 'required': True},
}

temperature_schema = {
    'time': {'type': 'integer', 'required': True},
    'activated': {'type': 'boolean', 'required': True},
    'readings_F': {'type': 'integer', 'required': True},
    'readings_C': {'type': 'integer', 'required': True},
}

speed_schema = {
    'time': {'type': 'integer', 'required': True},
    'activated': {'type': 'boolean', 'required': True},
    'mph': {'type': 'integer', 'required': True},
    'km': {'type': 'integer', 'required': True},
}

engine_schema = {
    'time': {'type': 'integer', 'required': True},
    'activated': {'type': 'boolean', 'required': True},
    'rpm': {'type': 'integer', 'required': True},
    'tire_health': {'type': 'string', 'required': True},
    'engine_health': {'type': 'string', 'required': True},
}

solar_schema = {
    'time': {'type': 'integer', 'required': True},
    'activated': {'type': 'boolean', 'required': True},
    'solar_collection': {'type': 'integer', 'required': True},
    'solar_health': {'type': 'string', 'required': True},
}

chasiss_schema = {
    'time': {'type': 'integer', 'required': True},
    'chassis_health': {'type': 'string', 'required': True},
}

def validate_data(data, schema):
    v = Validator(schema)
    return v.validate(data), v.errors
