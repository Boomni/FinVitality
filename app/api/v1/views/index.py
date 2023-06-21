#!/usr/bin/python3
""" View for the landing page"""
from app.api.v1 import app_views
from flask import jsonify, render_template
from flask import Flask, render_template, request, send_from_directory

@app_views.route('/', methods=['GET'], strict_slashes=False)
def homepage():
     """ FinVitality homepage """
     return "Viola :) Welcome"


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})
