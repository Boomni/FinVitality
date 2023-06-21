#!/usr/bin/python3
"""
This module instantiates an object of class DBStorage
"""

from app.api.v1.models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
