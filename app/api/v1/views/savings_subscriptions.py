#!/usr/bin/python3
""" Module for user authentication and login """

from flask import render_template, request, session, redirect
from app.api.v1.models.contribution_subscriptions import ContributionSubscription
from app.api.v1.models.users import User
from app.api.v1.models import storage
from app.api.v1 import app_views


@app_views.route('/user/subscriptions/savings', methods=['GET'], strict_slashes=False)
def display_savings_subscriptions():
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
            subscriptions = session_data.query(ContributionSubscription).filter(
                ContributionSubscription.user_id == user.id
            ).all()
            contribution_data = []
            for subscription in subscriptions:
                contribution_data.append({
                    'title': subscription.contribution.title,
                    'description': subscription.contribution.description,
                    'amount': subscription.contribution.amount,
                    'duration': subscription.contribution.duration,
                    'start_date': subscription.contribution.start_date,
                    'end_date': subscription.contribution.end_date,
                    'benefits': subscription.contribution.benefits
                })

            return render_template('savings_subscriptions.html',
                                   profile_data=profile_data,
                                   contribution_data=contribution_data,
                                   )