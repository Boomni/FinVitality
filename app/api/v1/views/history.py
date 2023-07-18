#!/usr/bin/python3
""" View for the transaction history page"""
from app.api.v1 import app_views
from flask import render_template, request
from flask import flash, session, redirect, url_for
from app.api.v1.models.transactions import Transaction
from app.api.v1.models import storage
from app.api.v1.models.users import User


@app_views.route('/user/transactions',
                 methods=['GET'], strict_slashes=False)
def get_transaction_history():
    """Displays an HTML page with a list of the transaction history"""
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
    transaction_data = storage.all(Transaction).values()
    return render_template('history.html', transaction_data=transaction_data, profile_data=profile_data)
