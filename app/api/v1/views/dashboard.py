#!/usr/bin/python3
""" Module for dashboard """

from flask import jsonify, render_template, session, redirect
from app.api.v1 import app_views


@app_views.route('/dashboard', strict_slashes=False)
def dashboard():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template("dashboard.html")