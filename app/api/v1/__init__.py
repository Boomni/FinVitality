#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

from .views.index import *
from .views.register import *
from .views.login import *
from .views.logout import *
from .views.dashboard import *
from .views.profile import *
from .views.contributions import *
from .views.loans import *
from .views.savings_subscriptions import *
from .views.loans_subscriptions import *
from .views.history import *
