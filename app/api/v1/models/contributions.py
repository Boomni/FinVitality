#!/usr/bin/python3
"""Contributions Module"""
from app.api.v1.models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Date, Numeric, Text
from sqlalchemy.sql import sqltypes
import json


class Contribution(BaseModel, Base):
    __tablename__ = 'contributions'
    id = Column(String(60), primary_key=True)
    title = Column(String(60), nullable=False)
    description = Column(String(255), nullable=False)
    amount = Column(Numeric(12, 2), nullable=False)
    duration = Column(String(30), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    benefits = Column(Text, nullable=True)

    def set_benefits(self, benefits):
        self.benefits = json.dumps(benefits)

    def get_benefits(self):
        if self.benefits:
            return json.loads(self.benefits)
        return []
