#!/usr/bin/python3
""" View for the loans page"""
from app.api.v1 import app_views
from flask import Flask, render_template, request, send_from_directory, abort, jsonify
from app.api.v1.models.loans import Loan
from app.api.v1.models import storage



@app_views.route('/loans', methods=['GET'], strict_slashes=False)
def loans_packages():
    """ displays a HTML page with a list of loans """
    loans = storage.all(Loan).values()
    loans = sorted(loans, key=lambda k: k.title)
    return render_template('loans.html', loans=loans)