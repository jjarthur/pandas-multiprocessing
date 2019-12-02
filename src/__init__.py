import os

from flask import Flask, jsonify
from . import data_handler

def create_app():
    app = Flask(__name__)

    @app.route("/data")
    def data():
        return jsonify(data_handler.data())

    return app
