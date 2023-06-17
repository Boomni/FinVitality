#!/usr/bin/python3
"""This module defines a class LoanApplication"""
from backend.app.models.base_model import BaseModel, Base
from backend.app.models.users import User
from backend.app.models.loans import Loan
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

