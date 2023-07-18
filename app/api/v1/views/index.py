#!/usr/bin/python3
""" View for the landing page"""
from app.api.v1 import app_views
from flask import flash, render_template, redirect
from flask import request
from flask_mail import Message


@app_views.route('/', methods=['GET'], strict_slashes=False)
def homepage():
    """ FinVitality homepage """
    return render_template("index.html")


@app_views.route('/', methods=['POST'], strict_slashes=False)
def contact_form():
    from app.api.v1.app import mail
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    msg = Message(subject, sender=email, recipients=['rejoiceoye1@gmail.com'])
    msg.body = message

    try:
        mail.send(msg)
        flash('Email sent successfully', 'success')
        return redirect('/#contact')
    except Exception as e:
        print(str(e))
        flash('Failed to send email', 'error')
        return redirect('/#contact')
