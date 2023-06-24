#!/usr/bin/python3
""" Module for user authentication and login """

from flask import jsonify, render_template, request, session, redirect
from app.api.v1 import app_views


@app_views.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    profile_data = session.get('profile_data')
    
    return render_template('profile.html', profile_data=profile_data)