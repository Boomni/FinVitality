#!/usr/bin/python3
'''database storage engine'''

import sqlalchemy
from sqlalchemy import create_engine
from app.api.v1 import models
from sqlalchemy.orm import sessionmaker, scoped_session
from app.api.v1.models.base_model import BaseModel, Base
from app.api.v1.models.loan_applications import LoanApplication
from app.api.v1.models.contributions import Contribution
from app.api.v1.models.loans import Loan
from app.api.v1.models.contribution_subscriptions import ContributionSubscription
from app.api.v1.models.transactions import Transaction
from app.api.v1.models.users import User
from os import getenv
from dotenv import load_dotenv


classes = {
    "User": User,
    "Loan": Loan,
    "Contribution": Contribution,
    "LoanApplication": LoanApplication,
    "ContributionSubscription": ContributionSubscription,
    "Transaction": Transaction
}


class DBStorage:
    '''database storage engine for mysql storage'''
    __engine = None
    __session = None

    def __init__(self):
        '''instantiate new dbstorage instance'''
        load_dotenv()
        USER = getenv('FinVitality_DB_USER')
        PWD = getenv('FinVitality_DB_PWD')
        HOST = getenv('FinVitality_DB_HOST')
        DB = getenv('FinVitality_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                                           USER,
                                           PWD,
                                           HOST,
                                           DB
                                       ), pool_pre_ping=True)

    def all(self, cls=None):
        '''query on the current db session all cls objects'''
        dictionary = {}
        if cls is None:
            for the_class in classes.values():
                objs = self.__session.query(the_class).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dictionary[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ + '.' + obj.id
                dictionary[key] = obj
        return dictionary

    def new(self, obj):
        '''adds the obj to the current db session'''
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        '''commit all changes of the current db session'''
        self.__session.commit()

    def delete(self, obj=None):
        ''' deletes from the current databse session the obj
            is it's not None
        '''
        if obj is not None:
            self.__session.query(
                type(obj)
            ).filter(type(obj).id == obj.id).delete()

    def reload(self):
        '''reloads the database'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False
        )
        self.__session = scoped_session(session_factory)
        self.__session.configure(bind=self.__engine)
        self.__session = self.__session()

    def close(self):
        """Remove the current session to create a new one"""
        self.__session.close()
    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

    def get_session(self):
        return self.__session

    def filter(self, cls, **kwargs):
        """
        Filter objects of a specific class based on the specified criteria (kwargs).
        Returns a list of filtered objects.
        """
        if cls not in classes.values():
            return []

        filtered_objects = []

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if all(getattr(value, attr) == val for attr, val in kwargs.items()):
                filtered_objects.append(value)

        return filtered_objects
