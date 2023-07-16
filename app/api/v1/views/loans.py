#!/usr/bin/python3
""" View for the loans page"""
from app.api.v1 import app_views
from flask import session, render_template
from app.api.v1.models.loans import Loan
from app.api.v1.models.users import User
from app.api.v1.models import storage


@app_views.route('/user/loans', methods=['GET'], strict_slashes=False)
def loans_packages():
    """ displays a HTML page with a list of loans """
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
            }
    loans = storage.all(Loan).values()
    loans = sorted(loans, key=lambda k: k.title)
    return render_template('loans.html', loans=loans, profile_data=profile_data)
