from flask import Blueprint, request
import datetime
import logging
import json
##get the import tb to call get_db()
from core.api.api_response import APIResponse, AddData, Battery, Temperature, Speed, Engine, Solar, Chassis

api = Blueprint("api", __name__)

#battery, temperature, rpm, speed, 
@api.route("/telemetry/data/", methods=["POST"])
def add_data_to_db():
    text = request.args.get("text")
    if not text:
        return APIResponse.error("No text provided", 400).make()
    db = get_db() ##need db to be set up
    cursor = db.cursor()
    cursor.execute("INSERT INTO data (text) VALUES (%s)", (text,)) ## Format this once we see data
    db.commit()
    
    return APIResponse.success(AddData(True)).make()


# @api.route("/telemetry/config/", methods=["GET"]) Might not need this

@api.route("/telemetry/battery/", methods=["GET"])
def get_battery_data():
    if Battery.data:
        return APIResponse.success(Battery).make()
    return APIResponse.success(AddData(True)).make()

@api.route("/telemetry/temperature/", methods=["GET"])
def get_temperature_data():
    if Temperature.data:
        return APIResponse.success(Temperature).make()
    return APIResponse.success(AddData(True)).make()

@api.route("/telemetry/speed/", methods=["GET"])
def get_speed_data():
    if Speed.data:
        return APIResponse.success(Speed).make()
    return APIResponse.success(AddData(True)).make()

@api.route("/telemetry/engine/", methods=["GET"])
def get_engine_data():
    if Engine.data:
        return APIResponse.success(Engine).make()
    return APIResponse.success(AddData(True)).make()

@api.route("/telemetry/solar/", methods=["GET"])
def get_solar_data():
    if Solar.data:
        return APIResponse.success(Solar).make()
    return APIResponse.success(AddData(True)).make()

@api.route("/telemetry/chassis/", methods=["GET"])
def get_chassis_data():
    if Chassis.data:
        return APIResponse.success(Chassis).make()
    return APIResponse.success(AddData(True)).make()
