#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    A class for the Amenity attributes
    """
    __tablename__ == 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary='place_amenity')

    def __init__(self, *args, **kwargs):
        """
        Initializes Amenity"""
        super().__init__(*args, **kwargs)
