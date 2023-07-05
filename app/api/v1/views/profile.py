#!/usr/bin/python3
""" Module for user authentication and login """

import os
from werkzeug.utils import secure_filename
from flask import render_template, request, session, redirect, flash, url_for, render_template, current_app
from app.api.v1.models.users import User
from app.api.v1.models import storage
from app.api.v1 import app_views


@app_views.route('/user/profile', methods=['GET'], strict_slashes=False)
def profile():
    if not session.get('logged_in'):
        return redirect('/login')
    user_email = session['email']
    session_data = storage.get_session()

    if session_data:
        user = session_data.query(User).filter(User.email == user_email).first()

        if user:
            profile_data = {
                'firstname': user.firstname,
                'lastname': user.lastname,
                'middle_name': user.middle_name,
                'birth_date': user.birth_date,
                'email': user.email,
                'password': user.password,
                'address': user.address,
                'phonenumber': user.phonenumber,
                'employment_status': user.employment_status,
                'profile_picture': user.profile_picture
            }
            return render_template('profile.html', profile_data=profile_data, filename=user.profile_picture)



@app_views.route('/user/profile/update', methods=['GET'], strict_slashes=False)
def display_profile_update_form():
    return render_template("profile_update.html")

@app_views.route('/user/profile/update', methods=['PUT'], strict_slashes=False)
def update_profile():
    middle_name = request.form['middle_name']
    birth_date = request.form['birth_date']
    password = request.form['password']
    address = request.form['address']
    employment_status = request.form['employment_status']
    profile_picture = request.form['profile_picture']

    session_data = storage.get_session()

    if confirm_pwd != password:
        flash('Passwords don\'t match', 'error')
        return redirect(url_for('app_views.display_profile_update_form'))

    user = User(
        middle_name=middle_name,
        birth_date=birth_date,
        password=generate_password_hash(password),
        address=address,
        employment_status=employment_status,
        profile_picture=profile_picture
    )

    session_data.add(user)
    session_data.commit()

    return redirect("/user/profile")

@app_views.route('/user/upload-photo', methods=['POST'], strict_slashes=False)
def upload_profile_photo():
    UPLOAD_FOLDER = 'app/api/v1/static/images/users/'
    if 'email' in session and 'logged_in' in session and session['logged_in']:
        user_email = session['email']
        session_data = storage.get_session()

        if session_data:
            user = session_data.query(User).filter(User.email == user_email).first()

            if user:
                if 'photo' not in request.files:
                    flash('No file part', 'error')
                    return redirect(request.url)

                photo = request.files['photo']

                if photo.filename == '':
                    flash('No selected file', 'error')
                    return redirect('/user/profile')

                if not allowed_file(photo.filename):
                    flash('Invalid file extension', 'error')
                    return redirect('/user/profile')

                filename = secure_filename(photo.filename)
                filename = generate_unique_filename(user.id, filename)

                delete_existing_profile_photo(user.id)

                photo.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

                user.profile_picture = filename
                session_data.commit()

                flash('Profile photo updated successfully', 'success')
                return redirect(url_for('app_views.profile', filename=filename))
    return redirect('/login')

def allowed_file(filename):
    """ Check if the file has an allowed extension """
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_unique_filename(user_id, filename):
    """ Generate a unique filename by appending the user ID """
    basename, extension = os.path.splitext(filename)
    return f"{user_id}{extension}"

def delete_existing_profile_photo(user_id):
    if 'email' in session and 'logged_in' in session and session['logged_in']:
        user_email = session['email']
        session_data = storage.get_session()

        if session_data:
            user = session_data.query(User).filter(User.email == user_email).first()

            if user:
                existing_photo = user.profile_picture

    if existing_photo:
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], existing_photo)
        if os.path.exists(filepath):
            os.remove(filepath)