#!/usr/bin/python3
"""Loans Module"""
from app.api.v1.models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql import sqltypes


class Loan(BaseModel, Base):
    __tablename__ = 'loans'
    id = Column(String(60), primary_key=True)
    amount = Column(sqltypes.Numeric(12, 2), nullable=False)
    interest_rate = Column(sqltypes.Numeric(5, 2))
    loan_term = Column(Integer, nullable=False)
