#!/usr/bin/python3
"""This module defines a class ContributionSubscription"""
from backend.app.models.base_model import BaseModel, Base
from backend.app.models.users import User
from backend.app.models.contributions import Contribution
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class ContributionSubscription(Base):
    __tablename__ = 'contribution_subscriptions'
    id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    contribution_id = Column(String(60), ForeignKey('contributions.id'), nullable=False)
    user = relationship("User")
    contribution = relationship("Contribution")
