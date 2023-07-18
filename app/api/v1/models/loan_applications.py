#!/usr/bin/python3
"""This module defines a class LoanApplication"""
from app.api.v1.models.base_model import BaseModel, Base
from app.api.v1.models.users import User
from app.api.v1.models.loans import Loan
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import sqltypes
from sqlalchemy import Integer, Numeric, Date, Text
from sqlalchemy.event import listens_for
import uuid

class LoanApplication(BaseModel, Base):
    __tablename__ = 'loan_applications'

    custom_id = Column(String(6), primary_key=True, unique=True, nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    interest_rate = Column(sqltypes.Numeric(5, 2))
    status = Column(String(10))
    firstname = Column(String(100))
    lastname = Column(String(100))
    marital_status = Column(String(100))
    date_of_birth = Column(Date)
    gender = Column(String(10))
    email = Column(String(128))
    mobile_number = Column(String(15))
    bank_name = Column(String(60))
    account_number = Column(String(15))
    bvn = Column(String(20))
    contact_information = Column(String(128))
    employment_status = Column(String(20))
    loan_credit_facility = Column(String(60))
    office_address = Column(String(128))
    occupation = Column(String(60))
    annual_income = Column(Numeric(15, 2))
    length_of_employment = Column(Integer)
    num_dependents = Column(Numeric(10, 2))
    collateral_details = Column(Text)
    loan_amount = Column(sqltypes.Numeric(12, 2))
    loan_purpose = Column(Text)
    user = relationship("User")

    _last_generated_number = 0

@staticmethod
@listens_for(LoanApplication, 'before_insert')
def generate_custom_id(mapper, connection, target):
    if not target.custom_id:
        LoanApplication._last_generated_number += 1
        target.custom_id = f'FL{LoanApplication._last_generated_number:03}'