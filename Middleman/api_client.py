import requests
import json
# import time
# import datetime


#{"BMS_temp_state", BMS_current_voltage", "VESC_set_duty_cycle", "VESC_status_1", "VESC_status_2", "VESC_status_3", "VESC_status_4", "VESC_status_5"}
def APIPost(status_type, data):
    #BACKEND HOST IS CURRENTLY SET ON 7000, local host, can be changed in 'main.py' in the backend folder
    uri_prefix = "http://localhost:7000/api/telemetry/"
    status_type_to_uri = {"BMS_temp_state": "bms/temp-state", "BMS_current_voltage": "bms/power/", "VESC_set_duty_cycle": "vesc/duty-cycle/", "VESC_status_1": "vesc/status/1", "VESC_status_2": "vesc/status/2", "VESC_status_3": "vesc/status/3", "VESC_status_4": "vesc/status/4", "VESC_status_5": "vesc/status/5"}
    uri = uri_prefix + status_type_to_uri[status_type]
    # print(uri)
    serialized_data = json.dumps(data)
    # print(serialized_data)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(uri, data=serialized_data, headers=headers)
    print("API POST: " + status_type)
    print("Status Code: " + str(r.status_code))
    print(r.text)
