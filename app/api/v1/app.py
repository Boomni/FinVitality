#!/usr/bin/python3
""" Flask Application """
import os
from flask import Flask, send_from_directory
from app.api.v1 import app_views
from app.api.v1.config import SECRET_KEY, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD


app = Flask(__name__)
app.register_blueprint(app_views)
ALLOWED_EXTENSIONS = {'png', 'jpg'}
app.config['SECRET_KEY'] = SECRET_KEY
UPLOAD_FOLDER = 'app/api/v1/static/images/users/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', threaded=True, debug=True)