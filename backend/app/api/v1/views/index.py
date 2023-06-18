#!/usr/bin/python3
""" View for the landing page"""
from backend.app.api.v1 import app_views
from flask import jsonify, render_template
from flask import Flask, render_template, request

app = Flask(__name__)

@app_views.route('/', methods=['GET'], strict_slashes=False)
def homepage():
    return "Viola :) Welcome"

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})
