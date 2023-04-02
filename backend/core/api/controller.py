from flask import Blueprint, request, url_for
from core.api.data_schema import battery_schema, temperature_schema, speed_schema, engine_schema, solar_schema, chassis_schema, validate_data
from core.api.db_convert import append_data, get_data_all, get_data

from core.api.api_response import APIResponse

api = Blueprint("api", __name__)

#As of 4/1/2023, the comments for each type of endpoint, Post, Get(no query), Get(id) are the same, comments for battery
#can be used to interpret for all the components: battery, temperature, speed, engine, solar, chassis

csv_file_path = "./core/csv_data/"

"""
Add data to the CSV file.
It validates the input data using the schema.
If the data is valid, it appends it to the CSV file and returns a success response.
If the data is invalid or could not be added to the CSV file, it returns an error response.
"""
@api.route("/telemetry/battery/", methods=["POST"])
def post_battery():
    data = request.get_json()
    if not data: return APIResponse.error("No data provided", 400).make()
    valid, error = validate_data(data, battery_schema) #validate data
    if not valid: return APIResponse.error(error, 400).make()
    id = append_data(csv_file_path + "battery.csv", battery_schema, data) #add data to csv
    if not id: return APIResponse.error("Failed to add data", 500).make()
    new_data_url = url_for('get_battery_data_by_id', id=id)
    return APIResponse.post_success(data, new_data_url).make()

"""
Retrieve all data from the CSV file.
If the data is retrieved successfully, it returns a success response with the retrieved data.
If the data could not be retrieved, it returns an error response.
"""
@api.route("/telemetry/battery/", methods=["GET"])
def get_battery_data():
    data = get_all_data(csv_file_path + "battery.csv", battery_schema)
    if not data: return APIResponse.error("Failed to get data or not found", 500).make()
    return APIResponse.get_success(data).make()

"""
Retrieve data from the CSV file with the specified id or timestamp.
If the data is retrieved successfully, it returns a success response with the retrieved data.
If the data could not be retrieved, it returns an error response.
"""
@api.route("/telemetry/battery/<int:id>", methods=["GET"])
def get_battery_data_by_id(id):
    time = request.args.get('time')
    if time: data = get_data_by_id(csv_file_path + "battery.csv", battery_schema, time=time)
    else: data = get_data_by_id(csv_file_path + "battery.csv", battery_schema, id=id)
    if not data: return APIResponse.error("Data not found", 404).make()
    return APIResponse.get_success(data).make()

@api.route("/telemetry/temperature/", methods=["POST"])
def post_temperature():
    data = request.get_json()
    if not data: return APIResponse.error("No data provided", 400).make()
    valid, error = validate_data(data, temperature_schema) #validate data
    if not valid: return APIResponse.error(error, 400).make()
    id = append_data(csv_file_path + "temperature.csv", temperature_schema, data) #add data to csv
    if not id: return APIResponse.error("Failed to add data", 500).make()
    new_data_url = url_for('get_temperature_data_by_id', id=id)
    return APIResponse.post_success(data, new_data_url).make()

@api.route("/telemetry/temperature/", methods=["GET"])
def get_temperature_data():
    data = get_all_data(csv_file_path + "temperature.csv", temperature_schema)
    if not data: return APIResponse.error("Failed to get data or not found", 500).make()
    return APIResponse.get_success(data).make()

@api.route("/telemetry/temperature/<int:id>", methods=["GET"])
def get_temperature_data_by_id(id):
    time = request.args.get('time')
    if time: data = get_data_by_id(csv_file_path + "temperature.csv", temperature_schema, time=time)
    else: data = get_data_by_id(csv_file_path + "temperature.csv", temperature_schema, id=id)
    if not data: return APIResponse.error("Data not found", 404).make()
    return APIResponse.get_success(data).make()

@api.route("/telemetry/speed/", methods=["POST"])
def post_speed():
    data = request.get_json()
    if not data: return APIResponse.error("No data provided", 400).make()
    valid, error = validate_data(data, speed_schema)
    if not valid: return APIResponse.error(error, 400).make()
    id = append_data(csv_file_path + "speed.csv", speed_schema, data)
    if not id: return APIResponse.error("Failed to add data", 500).make()
    new_data_url = url_for('get_speed_data_by_id', id=id)
    return APIResponse.post_success(data, new_data_url).make()

@api.route("/telemetry/speed/", methods=["GET"])
def get_speed_data():
    data = get_all_data(csv_file_path + "speed.csv", speed_schema)
    if not data: return APIResponse.error("Failed to get data or not found", 500).make()
    return APIResponse.get_success(data).make()

@api.route("/telemetry/speed/<int:id>", methods=["GET"])
def get_speed_data_by_id(id):
    time = request.args.get('time')
    if time: data = get_data_by_id(csv_file_path + "speed.csv", speed_schema, time=time)
    else: data = get_data_by_id(csv_file_path + "speed.csv", speed_schema, id=id)
    if not data: return APIResponse.error("Data not found", 404).make()
    return APIResponse.get_success(data).make()

@api.route("/telemetry/engine/", methods=["POST"])
def post_engine():
    data = request.get_json()
    if not data: return APIResponse.error("No data provided", 400).make()
    valid, error = validate_data(data, engine_schema)
    if not valid: return APIResponse.error(error, 400).make()
    id = append_data(csv_file_path + "engine.csv", engine_schema, data)
    if not id: return APIResponse.error("Failed to add data", 500).make()
    new_data_url = url_for('get_engine_data_by_id', id=id)
    return APIResponse.post_success(data, new_data_url).make()

@api.route("/telemetry/engine/", methods=["GET"])
def get_engine_data():
    data = get_all_data(csv_file_path + "engine.csv", engine_schema)
    if not data: return APIResponse.error("Failed to get data or not found", 500).make()
    return APIResponse.get_success(data).make()

@api.route("/telemetry/engine/<int:id>", methods=["GET"])
def get_engine_data_by_id(id):
    time = request.args.get('time')
    if time: data = get_data_by_id(csv_file_path + "engine.csv", engine_schema, time=time)
    else: data = get_data_by_id(csv_file_path + "engine.csv", engine_schema, id=id)
    if not data: return APIResponse.error("Data not found", 404).make()
    return APIResponse.get_success(data).make()

@api.route("/telemetry/solar/", methods=["POST"])
def post_solar():
    data = request.get_json()
    if not data: return APIResponse.error("No data provided", 400).make()
    valid, error = validate_data(data, solar_schema)
    if not valid: return APIResponse.error(error, 400).make()
    id = append_data(csv_file_path + "solar.csv", solar_schema, data)
    if not id: return APIResponse.error("Failed to add data", 500).make()
    new_data_url = url_for('get_solar_data_by_id', id=id)
    return APIResponse.post_success(data, new_data_url).make()

@api.route("/telemetry/solar/", methods=["GET"])
def get_solar_data():
    data = get_all_data(csv_file_path + "solar.csv", solar_schema)
    if not data: return APIResponse.error("Failed to get data or not found", 500).make()
    return APIResponse.get_success(data).make()

@api.route("/telemetry/solar/<int:id>", methods=["GET"])
def get_solar_data_by_id(id):
    time = request.args.get('time')
    if time: data = get_data_by_id(csv_file_path + "solar.csv", solar_schema, time=time)
    else: data = get_data_by_id(csv_file_path + "solar.csv", solar_schema, id=id)
    if not data: return APIResponse.error("Data not found", 404).make()
    return APIResponse.get_success(data).make()

@api.route("/telemetry/chassis/", methods=["POST"])
def post_chassis():
    data = request.get_json()
    if not data: return APIResponse.error("No data provided", 400).make()
    valid, error = validate_data(data, chassis_schema)
    if not valid: return APIResponse.error(error, 400).make()
    id = append_data(csv_file_path + "chassis.csv", chassis_schema, data)
    if not id: return APIResponse.error("Failed to add data", 500).make()
    new_data_url = url_for('get_chassis_data_by_id', id=id)
    return APIResponse.post_success(data, new_data_url).make()

@api.route("/telemetry/chassis/", methods=["GET"])
def get_chassis_data():
    data = get_all_data(csv_file_path + "chassis.csv", chassis_schema)
    if not data: return APIResponse.error("Failed to get data or not found", 500).make()
    return APIResponse.get_success(data).make()

@api.route("/telemetry/chassis/<int:id>", methods=["GET"])
def get_chassis_data_by_id(id):
    time = request.args.get('time')
    if time: data = get_data_by_id(csv_file_path + "chassis.csv", chassis_schema, time=time)
    else: data = get_data_by_id(csv_file_path + "chassis.csv", chassis_schema, id=id)
    if not data: return APIResponse.error("Data not found", 404).make()
    return APIResponse.get_success(data).make()

