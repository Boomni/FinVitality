#!/usr/bin/python3
""" Module for new user authentication """

from werkzeug.security import generate_password_hash
from app.api.v1.models.users import User
from app.api.v1.models import storage
from flask import render_template, request
from flask import flash, redirect, url_for, session
from app.api.v1 import app_views
import re


@app_views.route('/register', methods=['GET'], strict_slashes=False)
def display_registration_form():
    return render_template("register.html")


@app_views.route('/register', methods=['POST'], strict_slashes=False)
def authenticate_and_register():
    firstname = request.form.get("firstname")
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    password = request.form.get('password')
    phonenumber = request.form.get("phonenumber")
    confirm_pwd = request.form.get("confirm_pwd")

    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        flash('Invalid email address', 'error')
        return redirect(url_for('app_views.display_registration_form'))

    session_data = storage.get_session()

    if session_data.query(User).filter(User.email == email).first():
        flash('Email already exists', 'error')
        session['form_data'] = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'phonenumber': phonenumber
        }
        return redirect(url_for('app_views.display_registration_form'))

    if session_data.query(User).filter(User.phonenumber
                                       == phonenumber).first():
        flash('Phone number already exists', 'error')
        session['form_data'] = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'phonenumber': phonenumber
        }
        return redirect(url_for('app_views.display_registration_form'))

    if confirm_pwd != password:
        flash('Passwords don\'t match', 'error')
        session['form_data'] = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'phonenumber': phonenumber
        }
        return redirect(url_for('app_views.display_registration_form'))

    user = User(
        firstname=firstname,
        lastname=lastname,
        email=email,
        password=generate_password_hash(password),
        phonenumber=phonenumber
    )

    session_data.add(user)
    session_data.commit()

    return redirect("/user/dashboard")
