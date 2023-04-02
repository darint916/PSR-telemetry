from flask import Flask
from flask_cors import CORS
from core.api.controller import api

app = Flask(__name__)

app.register_blueprint(api, url_prefix="/api")

CORS(app)

cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})