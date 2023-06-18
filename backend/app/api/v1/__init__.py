#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from backend.app.api.v1.views.index import *
from backend.app.api.v1.views.register import *
