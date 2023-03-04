from typing import Type
from flask import jsonify

class Serializable:
    def serialize(self) -> dict:
        raise NotImplementedError()

class APIResponse:
    def __init__(self, is_error: bool, error_message:str, status: int, data: Type[Serializable]):
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
        'name': 'Battery',
        'activated': False,
        'percent': 0,
        'units': '%',
        'time': 0,
        'battery_health': 'Healthy',
    }
    @staticmethod
    def serialize(self)->dict:
        return Battery.data
    
class Temperature(Serializable):

    data = {
        'name': 'Thermostat',
        'activated': False,
        'readings_F': 0,
        'readings_C': 0,
        'units_F': 'F',
        'units_C': 'C',
        'time': 0,
    }

    @staticmethod
    def serialize(self)->dict:
        return Temperature.data

class Speed(Serializable):
    
    data = {
        'name': 'Speed',
        'activated': False,
        'meter': 'Odometer',
        'speed_mph': 0,
        'speed_km': 0,
        'units_mph': 'mph',
        'units_km': 'km',
        'time': 0,
    }

    @staticmethod
    def serialize(self)->dict:
        return Speed.data
    
class Engine(Serializable):
    
    data = {
        'name': 'Engine',
        'activated': False,
        'meter': 'Tachometer',
        'rpm': 0,
        'units': 'rpm',
        'time': 0,
        'tire_health': 'Healthy',
        'engine_health': 'Healthy',
    }

    @staticmethod
    def serialize(self)->dict:
        return Engine.data

class Solar(Serializable):

    data = {
        'name': 'Solar Energy Input',
        'activated': False,
        'solar_collection': 0,
        'units': '%',
        'solar_health': 'Healthy',
        'time': 0,
    }

    @staticmethod
    def serialize(self)->dict:
        return Solar.data

class Chassis(Serializable): #remove if no possible input for chasis integrity

    data = {
        'name': 'Chassis',
        'chassis_health': 'Healthy', 
    }   

    @staticmethod
    def serialize(self)->dict:
        return Chassis.data
