#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ Class for state attributes """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """
            Getter method for cities
            """
            from models import storage
            from models.city import City

            cities = storage.all(City)
            list = []

            for city in cities.values():
                if city.state_id == self.id:
                    list.append(city)

            return list
