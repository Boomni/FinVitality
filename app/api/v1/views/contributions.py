#!/usr/bin/python3
""" View for the contributions package page"""
from app.api.v1 import app_views
from flask import Flask, render_template, request
from flask import flash, session, redirect, url_for
from app.api.v1.models.contributions import Contribution
from app.api.v1.models.contribution_subscriptions import ContributionSubscription
from app.api.v1.models import storage
from app.api.v1.models.users import User


@app_views.route('/user/contributions',
                 methods=['GET'], strict_slashes=False)
def contribution_packages():
    """Displays an HTML page with a list of contributions"""
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
    contributions = storage.all(Contribution).values()
    contributions = sorted(contributions, key=lambda k: k.title)
    return render_template('contributions.html', contributions=contributions, profile_data=profile_data)

@app_views.route('/create_contribution',
                 methods=['GET'], strict_slashes=False)
def display_package_form():
    """Displays a form to create a contribution package"""
    return render_template("create_contribution.html")


@app_views.route('/subscribe/<contribution_id>', methods=['GET'], strict_slashes=False)
def subscribe(contribution_id):
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

            subscription = ContributionSubscription(
                user_id=user.id,
                contribution_id=contribution_id,
            )

            session_data.add(subscription)
            session_data.commit()
            
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

            flash('Subscribed successfully', 'success')
            return render_template('subscriptions.html', contribution_data=contribution_data, profile_data=profile_data)

    flash('Failed to subscribe', 'error')
    return render_template("contributions.html", profile_data=profile_data)

@app_views.route('/create_contribution',
                 methods=['POST'], strict_slashes=False)
def create_package():
    """Creates a contribution package"""
    title = request.form.get("title")
    description = request.form.get("description")
    amount = request.form.get("amount")
    duration = request.form.get("duration")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")
    benefits = request.form.get("benefits")

    contribution = Contribution(
        title=title,
        description=description,
        amount=amount,
        duration=duration,
        start_date=start_date,
        end_date=end_date,
        benefits=benefits
    )

    storage.new(contribution)
    storage.save()

    return redirect("/user/contributions")


@app_views.route('/update_contribution/<contribution_id>',
                 methods=['POST'], strict_slashes=False)
def update_contribution(contribution_id):
    """Updates a contribution package"""
    contribution = storage.get(Contribution, contribution_id)
    if contribution:
        contribution.title = request.form.get("title")
        contribution.description = request.form.get("description")
        contribution.amount = request.form.get("amount")
        contribution.duration = request.form.get("duration")
        contribution.start_date = request.form.get("start_date")
        contribution.end_date = request.form.get("end_date")
        contribution.benefits = request.form.get("benefits")
        storage.save()
        return redirect("/contributions")
    else:
        flash('Contribution package not found', 'error')
        return redirect(url_for('contribution_packages'))


@app_views.route('/delete_contribution/<contribution_id>',
                 methods=['POST'], strict_slashes=False)
def delete_contribution(contribution_id):
    """Deletes a contribution package"""
    contribution = storage.get(Contribution, contribution_id)
    if contribution:
        storage.delete(contribution)
        storage.save()
        return redirect("/contributions")
    else:
        flash('Contribution package not found', 'error')
        return redirect(url_for('contribution_packages'))
