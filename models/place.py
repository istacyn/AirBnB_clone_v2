#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A class for place attributes """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        reviews = relationship('Review',
                               cascade='all, delete', backref='place')
        amenities = relationship('Amenity',
                                 secondary='place_amenity', viewonly=False)

    else:
        @property
        def reviews(self):
            """
            Returns the list of Review instances.
            """
            list_of_reviews = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    list_of_reviews.append(review)
            return list_of_reviews

        @property
        def amenities(self):
            """
            Getter attribute amenities
            """
            amenity_objs = []
            amenities = models.storage.all(Amenity)
            for amenity in amenities.values():
                if amenity.id in self.amenity_ids:
                    amenity_objs.append(amenity)
            return amenity_objs

        @amenities.setter
        def amenities(self, obj):
            """
            Setter attribute amenities"""
            if isinstance(obj, Amenity):
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        metadata = Base.metadata
        place_amenity = Table('place_amenity', metedata,
                              Column('place_id',
                                     String(60)
                                     ForeignKey('places.id'),
                                     primary_key=True,
                                     nullable=False),
                              Column('amenity_id',
                                     String(60)
                                     ForeignKey('amenities.id'),
                                     primary_key=True,
                                     nullable=False))

    def __inti__(self, *args, **kwargs):
        """
        Initialize places"""
        super().__inti__(*args, **kwargs)
