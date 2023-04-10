from flask import Blueprint, request, url_for
from core.api.data_schema import battery_schema, temperature_schema, speed_schema, engine_schema, solar_schema, chassis_schema, validate_data, vesc_duty_cycle_schema, vesc_stat1_schema, vesc_stat2_schema, vesc_stat3_schema, vesc_stat4_schema, vesc_stat5_schema, bms_power_schema, bms_temp_state_schema
from core.api.db_convert import append_data, get_data_all, get_data

from core.api.api_response import APIResponse, AddData, GetData

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
def general_post(file_name, schema, data, get_uri_location):
    if not data: return APIResponse.error("No data provided", 400).make()
    valid, error = validate_data(data, schema)
    if not valid: return APIResponse.error(error, 400).make()
    id = append_data(csv_file_path + file_name, schema, data)
    if not id: return APIResponse.error("Failed to add data", 500).make()
    new_data_url = url_for(get_uri_location, id=id, file_name=file_name)
    return APIResponse.post_success(AddData(True, id, file_name), new_data_url).make()


"""
Retrieve all data from the CSV file.
If the data is retrieved successfully, it returns a success response with the retrieved data.
If the data could not be retrieved, it returns an error response.
"""
def general_get_all(file_name, schema):
    data = get_data_all(csv_file_path + file_name, schema)
    if not data: return APIResponse.error("Failed to get data or not found", 500).make()
    return APIResponse.get_success(GetData(True, data)).make()

"""
Retrieve data from the CSV file with the specified id or timestamp.
If the data is retrieved successfully, it returns a success response with the retrieved data.
If the data could not be retrieved, it returns an error response.
"""
def general_get_by_id(file_name, schema, id, time):
    if time: data = get_data(csv_file_path + file_name, schema, time=time)
    else: data = get_data(csv_file_path + file_name, schema, id=id)
    if not data: return APIResponse.error("Data not found", 404).make()
    return APIResponse.get_success(GetData(True, data)).make()


#API ENDPOINTS

#VESC
@api.route("/telemetry/vesc/status/1", methods=["POST"])
def post_vesc_status():
    return general_post("vesc_status1.csv", vesc_stat1_schema, request.get_json(), 'api.get_vesc_status1_by_id')

@api.route("/telemetry/vesc/status/1", methods=["GET"])
def get_vesc_status1():
    return general_get_all("vesc_status1.csv", vesc_stat1_schema)

@api.route("/telemetry/vesc/status/1/<int:id>", methods=["GET"])
def get_vesc_status1_by_id(id):
    return general_get_by_id("vesc_status1.csv", vesc_stat1_schema, id, request.args.get('time'))

@api.route("/telemetry/vesc/status/2", methods=["POST"])
def post_vesc_status2():
    return general_post("vesc_status2.csv", vesc_stat2_schema, request.get_json(), 'api.get_vesc_status2_by_id')

@api.route("/telemetry/vesc/status/2", methods=["GET"])
def get_vesc_status2():
    return general_get_all("vesc_status2.csv", vesc_stat2_schema)

@api.route("/telemetry/vesc/status/2/<int:id>", methods=["GET"])
def get_vesc_status2_by_id(id):
    return general_get_by_id("vesc_status2.csv", vesc_stat2_schema, id, request.args.get('time'))

@api.route("/telemetry/vesc/status/3", methods=["POST"])
def post_vesc_status3():
    return general_post("vesc_status3.csv", vesc_stat3_schema, request.get_json(), 'api.get_vesc_status3_by_id')

@api.route("/telemetry/vesc/status/3", methods=["GET"])
def get_vesc_status3():
    return general_get_all("vesc_status3.csv", vesc_stat3_schema)

@api.route("/telemetry/vesc/status/3/<int:id>", methods=["GET"])
def get_vesc_status3_by_id(id):
    return general_get_by_id("vesc_status3.csv", vesc_stat3_schema, id, request.args.get('time'))

@api.route("/telemetry/vesc/status/4", methods=["POST"])
def post_vesc_status4():
    return general_post("vesc_status4.csv", vesc_stat4_schema, request.get_json(), 'api.get_vesc_status4_by_id')

@api.route("/telemetry/vesc/status/4", methods=["GET"])
def get_vesc_status4():
    return general_get_all("vesc_status4.csv", vesc_stat4_schema)

@api.route("/telemetry/vesc/status/4/<int:id>", methods=["GET"])
def get_vesc_status4_by_id(id):
    return general_get_by_id("vesc_status4.csv", vesc_stat4_schema, id, request.args.get('time'))

@api.route("/telemetry/vesc/status/5", methods=["POST"])
def post_vesc_status5():
    return general_post("vesc_status5.csv", vesc_stat5_schema, request.get_json(), 'api.get_vesc_status5_by_id')

@api.route("/telemetry/vesc/status/5", methods=["GET"])
def get_vesc_status5():
    return general_get_all("vesc_status5.csv", vesc_stat5_schema)

@api.route("/telemetry/vesc/status/5/<int:id>", methods=["GET"])
def get_vesc_status5_by_id(id):
    return general_get_by_id("vesc_status5.csv", vesc_stat5_schema, id, request.args.get('time'))

@api.route("/telemetry/vesc/duty-cycle", methods=["POST"])
def post_vesc_duty_cycle():
    return general_post("vesc_duty_cycle.csv", vesc_duty_cycle_schema, request.get_json(), 'api.get_vesc_duty_cycle_by_id')

@api.route("/telemetry/vesc/duty-cycle", methods=["GET"])
def get_vesc_duty_cycle():
    return general_get_all("vesc_duty_cycle.csv", vesc_duty_cycle_schema)

@api.route("/telemetry/vesc/duty-cycle/<int:id>", methods=["GET"])
def get_vesc_duty_cycle_by_id(id):
    return general_get_by_id("vesc_duty_cycle.csv", vesc_duty_cycle_schema, id, request.args.get('time'))

#BMS
@api.route("/telemetry/bms/temp-state", methods=["POST"])
def post_bms_temp_state():
    return general_post("bms_temp_state.csv", bms_temp_state_schema, request.get_json(), 'api.get_bms_temp_state_by_id')

@api.route("/telemetry/bms/temp-state", methods=["GET"])
def get_bms_temp_state():
    return general_get_all("bms_temp_state.csv", bms_temp_state_schema)

@api.route("/telemetry/bms/temp-state/<int:id>", methods=["GET"])
def get_bms_temp_state_by_id(id):
    return general_get_by_id("bms_temp_state.csv", bms_temp_state_schema, id, request.args.get('time'))

@api.route("/telemetry/bms/power", methods=["POST"])
def post_bms_power():
    return general_post("bms_power.csv", bms_power_schema, request.get_json(), 'api.get_bms_power_by_id')

@api.route("/telemetry/bms/power", methods=["GET"])
def get_bms_power():
    return general_get_all("bms_power.csv", bms_power_schema)

@api.route("/telemetry/bms/power/<int:id>", methods=["GET"])
def get_bms_power_by_id(id):
    return general_get_by_id("bms_power.csv", bms_power_schema, id, request.args.get('time'))

#OTHERS
@api.route("/telemetry/battery/", methods=["POST"])
def post_battery():
    return general_post("battery.csv", battery_schema, request.get_json(), 'api.get_battery_data_by_id')

@api.route("/telemetry/battery/", methods=["GET"])
def get_battery_data():
    return general_get_all("battery.csv", battery_schema)

@api.route("/telemetry/battery/<int:id>", methods=["GET"])
def get_battery_data_by_id(id):
    return general_get_by_id("battery.csv", battery_schema, id, request.args.get('time'))

@api.route("/telemetry/temperature/", methods=["POST"])
def post_temperature():
    return general_post("temperature.csv", temperature_schema, request.get_json(), 'api.get_temperature_data_by_id')

@api.route("/telemetry/temperature/", methods=["GET"])
def get_temperature_data():
    return general_get_all("temperature.csv", temperature_schema)

@api.route("/telemetry/temperature/<int:id>", methods=["GET"])
def get_temperature_data_by_id(id):
    return general_get_by_id("temperature.csv", temperature_schema, id, request.args.get('time'))

@api.route("/telemetry/speed/", methods=["POST"])
def post_speed():
    return general_post("speed.csv", speed_schema, request.get_json(), 'api.get_speed_data_by_id')

@api.route("/telemetry/speed/", methods=["GET"])
def get_speed_data():
    return general_get_all("speed.csv", speed_schema)

@api.route("/telemetry/speed/<int:id>", methods=["GET"])
def get_speed_data_by_id(id):
    return general_get_by_id("speed.csv", speed_schema, id, request.args.get('time'))

@api.route("/telemetry/engine/", methods=["POST"])
def post_engine():
    return general_post("engine.csv", engine_schema, request.get_json(), 'api.get_engine_data_by_id')

@api.route("/telemetry/engine/", methods=["GET"])
def get_engine_data():
    return general_get_all("engine.csv", engine_schema)

@api.route("/telemetry/engine/<int:id>", methods=["GET"])
def get_engine_data_by_id(id):
    return general_get_by_id("engine.csv", engine_schema, id, request.args.get('time'))

@api.route("/telemetry/solar/", methods=["POST"])
def post_solar():
    return general_post("solar.csv", solar_schema, request.get_json(), 'api.get_solar_data_by_id')

@api.route("/telemetry/solar/", methods=["GET"])
def get_solar_data():
    return general_get_all("solar.csv", solar_schema)

@api.route("/telemetry/solar/<int:id>", methods=["GET"])
def get_solar_data_by_id(id):
    return general_get_by_id("solar.csv", solar_schema, id, request.args.get('time'))

@api.route("/telemetry/chassis/", methods=["POST"])
def post_chassis():
    return general_post("chassis.csv", chassis_schema, request.get_json(), 'api.get_chassis_data_by_id')

@api.route("/telemetry/chassis/", methods=["GET"])
def get_chassis_data():
    return general_get_all("chassis.csv", chassis_schema)

@api.route("/telemetry/chassis/<int:id>", methods=["GET"])
def get_chassis_data_by_id(id):
    return general_get_by_id("chassis.csv", chassis_schema, id, request.args.get('time'))
