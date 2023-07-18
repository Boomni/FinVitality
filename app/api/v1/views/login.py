#!/usr/bin/python3
""" Module for user authentication and login """

from flask import render_template, request, session, redirect, flash
from app.api.v1.models.users import User
from app.api.v1.models import storage
from werkzeug.security import check_password_hash
from app.api.v1 import app_views


@app_views.route('/login', methods=['GET'], strict_slashes=False)
def display_login_form():
    if session.get('logged_in'):
        return redirect('/user/dashboard')
    return render_template("login.html")


@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():
    email = request.form['email']
    password = request.form['password']

    session_data = storage.get_session()

    user = session_data.query(User).filter(User.email == email).first()
    if not user:
        flash('Password or Email is incorrect', 'error')
        session['form_data'] = {
            'email': email,
        }
        return redirect('/login')
    if not check_password_hash(user.password, password):
        flash('Password or Email is incorrect', 'error')
        session['form_data'] = {
            'email': email,
        }
        return redirect('/login')

    session['email'] = email
    session['logged_in'] = True

    return redirect('/user/dashboard')
