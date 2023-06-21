#!/usr/bin/python3
"""This module defines a class LoanApplication"""
from app.api.v1.models.base_model import BaseModel, Base
from app.api.v1.models.users import User
from app.api.v1.models.loans import Loan
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import sqltypes


class LoanApplication(BaseModel, Base):
    __tablename__ = 'loan_applications'
    id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    loan_id = Column(String(60), ForeignKey('loans.id'), nullable=False)
    amount = Column(sqltypes.Numeric(12, 2), nullable=False)
    status = Column(String(10), nullable=False)
    user = relationship("User")
    loan = relationship("Loan")
