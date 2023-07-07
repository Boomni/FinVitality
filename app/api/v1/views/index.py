#!/usr/bin/python3
""" View for the landing page"""
from app.api.v1 import app_views
from flask import jsonify, render_template
from flask import Flask, render_template, request, session
from flask_mail import Message
from app.api.v1.app import app, mail


@app_views.route('/', methods=['GET'], strict_slashes=False)
def homepage():
    """ FinVitality homepage """
    return render_template("index.html")


@app_views.route('/', methods=['POST'], strict_slashes=False)
def contact_form():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    msg = Message(subject, sender=email, recipients=['rejoiceoye1@gmail.com'])
    msg.body = message

    try:
        mail.send(msg)
        return 'Email sent successfully'
    except Exception as e:
        print(str(e))
        return 'Failed to send email'
