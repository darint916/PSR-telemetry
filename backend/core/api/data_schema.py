from cerberus import Validator
import datetime
from typing import Union

#converts string to datetime, returns string if fails, used in schema validation
def string_to_datetime(string: str) -> Union[datetime.datetime, str]:
    try:
        return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return str

#validates data against schema, returns tuple of bool and error message
def validate_data(data: dict, schema) -> tuple[bool, str]:
    v = Validator(schema)
    if not v.validate(data):
        error_messages = '\n'.join([f"{field}: {', '.join(errors)}" for field, errors in v.errors.items()])
        error_message = f"Data validation failed:\n{error_messages}"
        return False, error_message
    return True, None

battery_schema = {
    'time': {'type': 'datetime', 'required': True, 'coerce': string_to_datetime},
    'activated': {'type': 'boolean', 'required': True},
    'percent': {'type': 'integer', 'required': True, 'min': 0},
    'battery_health': {'type': 'string', 'required': True, 'allowed': ['healthy', 'warning', 'critical']},
}

temperature_schema = {
    'time': {'type': 'datetime', 'required': True, 'coerce': string_to_datetime},
    'activated': {'type': 'boolean', 'required': True},
    'temp_F': {'type': 'integer', 'required': True},
    'temp_c': {'type': 'integer', 'required': True},
}

speed_schema = {
    'time': {'type': 'datetime', 'required': True, 'coerce': string_to_datetime},
    'activated': {'type': 'boolean', 'required': True},
    'mph': {'type': 'integer', 'required': True},
    'km': {'type': 'integer', 'required': True,},
}

engine_schema = {
    'time': {'type': 'datetime', 'required': True, 'coerce': string_to_datetime},
    'activated': {'type': 'boolean', 'required': True},
    'rpm': {'type': 'integer', 'required': True, 'min': 0},
    'tire_health': {'type': 'string', 'required': True, 'allowed': ['healthy', 'warning', 'critical']},
    'engine_health': {'type': 'string', 'required': True, 'allowed': ['healthy', 'warning', 'critical']},
}

solar_schema = {
    'time': {'type': 'datetime', 'required': True, 'coerce': string_to_datetime},
    'activated': {'type': 'boolean', 'required': True},
    'power_generated': {'type': 'integer', 'required': True},
    'solar_health': {'type': 'string', 'required': True, 'allowed': ['healthy', 'warning', 'critical']},
}

chassis_schema = {
    'time': {'type': 'datetime', 'required': True, 'coerce': string_to_datetime},
    'chassis_health': {'type': 'string', 'required': True, 'allowed': ['healthy', 'warning', 'critical']},
}

