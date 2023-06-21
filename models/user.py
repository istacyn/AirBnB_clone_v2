#!/usr/bin/python3
"""This module defines a class User"""
import hashlib
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        _password = Column('password', String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place',
                              cascade='all, delete-orphan',
                              backref='user')
        reviews = relationship('Review',
                              cascade='all, delete-orphan',
                              backref='user')

    else:
        email = ''
        _password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """Intializes  an instance of User"""
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        """Accesses _password attribute"""
        return self._password

    @password.setter
    def password(self, pwd):
        """Perfoms hashing on password"""
        self._password = pwd
