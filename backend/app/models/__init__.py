#!/usr/bin/python3
"""
This module instantiates an object of class DBStorage
"""

from backend.app.models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
