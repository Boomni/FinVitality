#!/usr/bin/python3
""" Module for user authentication and logout"""

from flask import session, render_template, redirect
from app.api.v1 import app_views


@app_views.route('/logout', methods=['GET'], strict_slashes=False)
def logout():
    session.clear()

    return redirect('/login')