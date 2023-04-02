from typing import Type
from flask import jsonify

class Serializable:
    def serialize(self) -> dict:
        raise NotImplementedError()

#Init defines all possible data that could be stored in temp storage (obj instance)
class APIResponse:
    def __init__(self, is_error: bool, error_message:str, status: int, data: Type[Serializable], uri: str = None):
        self.is_error = is_error
        self.error_message = error_message
        self.status = status #status code of the response
        self.data = data #The data payload of the API response.
        self.uri = uri  #The URI of the resource that was created, if applicable. Defaults to None.
        
    def serialize_response_body(self) -> dict:
        if (self.data):
            return self.data.serialize()
        return None
    
    #What is returned to the client upon api call, can be used to limit or add more to the response
    def make(self):
        base = {
            "isError": self.is_error,
            "errorMessage": self.error_message,
            "response": self.serialize_response_body()
        }
        if (self.uri): #for post requests
            return jsonify(base), self.status, {'Location': self.uri} #probably a better way to add uri to header
        return jsonify(base), self.status
    
    
    '''these static methods are wrappers for API Responses with codes depending on method'''
    #for error responses
    @staticmethod
    def error(message: str, status: int) -> 'APIResponse':
        return APIResponse(True, message, status, None)
    
    #for get requests
    @staticmethod
    def get_success(data: dict) -> 'APIResponse':
        return APIResponse(False, "Success", 200, data)
    
    #for post requests
    @staticmethod
    def post_success(data: dict, location: str) -> 'APIResponse': 
        return APIResponse(False, "Success", 201, data, location)
    
'''DTOS essentially, output JSON formatting'''   
#Define Post response data payload
class AddData(Serializable):
    def __init__(self, success: bool, id: int, schema: str):
        self.success = success
        self.id = id
        self.schema = schema #Schema name
        
    def serialize(self) -> dict:
        return {
            'success': self.success,
            'id': self.id,
            'schema': self.schema
        }

#Define Get response data payload
class GetData(Serializable):
    def __init__(self, success: bool, data: dict):
        self.success = success
        self.data = data
        
    def serialize(self) -> dict:
        return {
            'success': self.success,
            'data': self.data
        }