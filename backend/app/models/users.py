#!/usr/bin/python3
"""This module defines a class User"""
from backend.app.models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Date, Text
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This is the User class"""

    __tablename__ = 'users'
    id = Column(String(60), primary_key=True)
    firstname = Column(String(128), nullable=False)
    lastname = Column(String(128), nullable=False)
    middle_name= Column(String(128))
    birth_date = Column(Date)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    address = Column(Text)
    phone_number = Column(String(15), nullable=False)
    employment_status = Column(String(60))
