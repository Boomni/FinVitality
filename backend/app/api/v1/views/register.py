#!/usr/bin/python3
""" Module for new user authentication """

from werkzeug.security import generate_password_hash
from backend.app.api.v1.models.users import User
from backend.app.api.v1.models import storage
from flask import jsonify, render_template, request
from backend.app.api.v1 import app_views


@app_views.route('/register', methods=['GET'], strict_slashes=False)
def show_registration_form():
    return render_template('register.html')


@app_views.route('/register', methods=['POST'], strict_slashes=False)
def authenticate_and_register():
    firstname = request.form["firstname"]
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    phone_number = request.form["phone_number"]

    session = storage.get_session()

    if session.query(User).filter(User.email == email).first():
        return jsonify({'message': 'Email already exists'}), 400

    if session.query(User).filter(User.phone_number == phone_number).first():
        return jsonify({'message': 'Phone number already exists'}), 400

    user = User(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=generate_password_hash(password),
            phone_number=phone_number
    )

    session.add(user)
    session.commit()

    return jsonify({'message': 'Registration successful'})
