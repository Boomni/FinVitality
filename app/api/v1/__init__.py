#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from app.api.v1.views.index import *
from app.api.v1.views.register import *
from app.api.v1.views.login import *
from app.api.v1.views.logout import *
from app.api.v1.views.dashboard import *
from app.api.v1.views.profile import *
from app.api.v1.views.contributions import *
from app.api.v1.views.loans import *
