#!/usr/bin/python3
""" Module for user authentication and login """

from flask import render_template, request, session, redirect
from app.api.v1.models.users import User
from app.api.v1.models.loan_applications import LoanApplication
from app.api.v1.models import storage
from app.api.v1 import app_views


@app_views.route('/user/subscriptions/loans', methods=['GET'], strict_slashes=False)
def display_loan_subscriptions():
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
            }

            loans = session_data.query(LoanApplication).filter(
                LoanApplication.user_id == user.id
            ).all()
            loan_data = []
            for loan in loans:
                loan_data.append({
                    'loan_id': loan.custom_id,
                    'firstname': loan.firstname,
                    'lastname': loan.lastname,
                    'loan_amount': loan.loan_amount,
                    'loan_purpose': loan.loan_purpose,
                    'status': loan.status
                })

            return render_template('loan_subscriptions.html',
                                   profile_data=profile_data,
                                   loan_data=loan_data
                                   )