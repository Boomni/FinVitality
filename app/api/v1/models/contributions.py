#!/usr/bin/python3
"""Contributions Module"""
from app.api.v1.models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Date
from sqlalchemy.sql import sqltypes


class Contribution(BaseModel, Base):
    __tablename__ = 'contributions'
    id = Column(String(60), primary_key=True)
    package = Column(String(60), nullable=False)
    description = Column(String(255), nullable=False)
    amount = Column(sqltypes.Numeric(12, 2), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
