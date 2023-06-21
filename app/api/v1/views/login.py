#!/usr/bin/python3
""" Module for user authentication and login """

from flask import jsonify, render_template, request, session, redirect
from app.api.v1.models.users import User
from app.api.v1.models import storage
from werkzeug.security import check_password_hash, generate_password_hash
from app.api.v1 import app_views


@app_views.route('/login', methods=['GET'], strict_slashes=False)
def display_login_form():
    return render_template("login.html")

@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():
    email = request.form['email']
    password = request.form['password']

    session_data = storage.get_session()

    user = session_data.query(User).filter(User.email == email).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404
    if not check_password_hash(user.password, password):
        return jsonify({'message': 'Password is incorrect'}), 401
    if not user and not check_password_hash(user-pwd, password):
        return jsonify({'message': 'Invalid email or password'}), 401

    session['email'] = email
    
    return jsonify({"message": "login successful"})