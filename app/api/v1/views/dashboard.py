""" Module for dashboard """

from app.api.v1.models.users import User
from app.api.v1.models import storage
from app.api.v1 import app_views
from flask import render_template, session, redirect


@app_views.route('/user/dashboard', strict_slashes=False)
def dashboard():
    if not session.get('logged_in'):
        return redirect('/login')
    user_email = session['email']
    session_data = storage.get_session()

    if session_data:
        user = session_data.query(User).filter(User.email
                                               == user_email).first()

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

            return render_template("dashboard.html",
                                   profile_data=profile_data,
                                   filename=user.profile_picture
                                   )
