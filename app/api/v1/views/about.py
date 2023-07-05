#!/usr/bin/python3
""" View for the about page"""
from app.api.v1 import app_views
from flask import Flask, render_template, request, send_from_directory, abort, jsonify


@app_views.route('/about', methods=['GET'], strict_slashes=False)
def about():
    """ Displays a HTML page with the about session """
    return render_template('about.html')