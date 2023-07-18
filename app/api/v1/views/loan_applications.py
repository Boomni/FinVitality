#!/usr/bin/python3
""" Module for new user authentication """

from app.api.v1.models.users import User
from app.api.v1.models import storage
from flask import jsonify, render_template, request
from flask import flash, redirect, url_for, session
from app.api.v1 import app_views
import re

