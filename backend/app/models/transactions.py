#!/usr/bin/python3
"""Transactions Module"""
from backend.app.models.base_model import BaseModel, Base
from backend.app.models.users import User
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import sqltypes


class Transaction(BaseModel, Base):
    __tablename__ = 'transactions'
    id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    transaction_type = Column(String(60), nullable=False)
    amount = Column(sqltypes.Numeric(12, 2), nullable=False)
    user = relationship("User")
