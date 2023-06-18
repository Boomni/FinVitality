#!/usr/bin/python3
""" Flask Application """
from flask import Flask, render_template, jsonify
from backend.app.api.v1 import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True, debug=True)
