from flask import Blueprint, request
import datetime
import logging
import json

from core.api.api_response import APIResponse, AddData, Config, InterceptedJson

api = Blueprint("api", __name__)

#battery, temperature, rpm, speed, 
@api.route("/", methods=["GET"])