from typing import Type
from flask import jsonify

class Serializable:
    def serialize(self) -> dict:
        raise NotImplementedError()

class APIResponse:
    def __init__(self, is_error: bool, error_message:str, status: int, data: Type[Serializable]) -> None:
        self.is_error = is_error
        self.error_message = error_message
        self.status = status
        self.data = data
    
    def serialize_data(self) -> dict:
        if (self.data):
            return self.data.serialize()
        return None
    
    def make(self):
        return jsonify({
            "is_error": self.is_error,
            "error_message": self.error_message,
            "data": self.serialize_data()
        })
    
    @staticmethod
    def error(message, status):
        return APIResponse(True, message, status, None)
    
    @staticmethod
    def success(data):
        return APIResponse(False, "Success", 200, data)

class AddData(Serializable):
    def __init__(self, success) -> None:
        self.success = success
    
    def serialize(self) -> dict:
        return {
            "success": self.success
        }

class Battery(Serializable):
    
    data = {
        'activated': False,
        'name': 'Battery',
        'percent': 0,
    }
    @staticmethod
    def serialize(self)->dict:
        return Battery.data
    
class Temperature(Serializable):

    data = {
        'activated': False,
        'name': 'Thermostat',
        'readings_F': 0,
        'readings_C': 0,
    }
    @staticmethod
    def serialize(self)->dict:
        return Temperature.data

class Speed(Serializable):
    
    data = {
        'activated': False,
        'name': 'Odometer',
        'speed_mph': 0,
        'speed_km': 0,
    }
    @staticmethod
    def serialize(self)->dict:
        return Speed.data
    
class Rotation:
    
    data = {
        'activated': False,
        'name': 'Tachometer',
    }