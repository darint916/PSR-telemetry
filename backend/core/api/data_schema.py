from cerberus import Validator

battery_schema = {
    'time': {'type': 'datetime', 'required': True},
    'activated': {'type': 'boolean', 'required': True},
    'percent': {'type': 'integer', 'required': True, 'min': 0},
    'battery_health': {'type': 'string', 'required': True, 'allowed': ['healthy', 'warning', 'critical']},
}

temperature_schema = {
    'time': {'type': 'datetime', 'required': True},
    'activated': {'type': 'boolean', 'required': True},
    'temp_F': {'type': 'integer', 'required': True},
    'temp_c': {'type': 'integer', 'required': True},
}

speed_schema = {
    'time': {'type': 'datetime', 'required': True},
    'activated': {'type': 'boolean', 'required': True},
    'mph': {'type': 'integer', 'required': True},
    'km': {'type': 'integer', 'required': True,},
}

engine_schema = {
    'time': {'type': 'datetime', 'required': True},
    'activated': {'type': 'boolean', 'required': True},
    'rpm': {'type': 'integer', 'required': True, 'min': 0},
    'tire_health': {'type': 'string', 'required': True, 'allowed': ['healthy', 'warning', 'critical']},
    'engine_health': {'type': 'string', 'required': True, 'allowed': ['healthy', 'warning', 'critical']},
}

solar_schema = {
    'time': {'type': 'datetime', 'required': True},
    'activated': {'type': 'boolean', 'required': True},
    'power_generated': {'type': 'integer', 'required': True},
    'solar_health': {'type': 'string', 'required': True, 'allowed': ['healthy', 'warning', 'critical']},
}

chasiss_schema = {
    'time': {'type': 'datetime', 'required': True},
    'chassis_health': {'type': 'string', 'required': True, 'allowed': ['healthy', 'warning', 'critical']},
}

def validate_data(data, schema):
    v = Validator(schema)
    return v.validate(data), v.errors
