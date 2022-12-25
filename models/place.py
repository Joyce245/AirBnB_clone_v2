#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
import os
import models


metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             nullable=False,
                             primary_key=True),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             nullable=False,
                             primary_key=True))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        review = relationship("Review", backref="place",
                              cascade="all, delete, delete-orphan")
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """Return all the reviews for this place.id"""
            objects = models.storage.all(Review)
            res = []
            for key, value in objects.items():
                if value.place_id == self.id:
                    res.append(value)
            return res

        @property
        def amenities(self):
            """Getter attr that return list of Amenity instances"""
            objects = models.storage.all(Amenity)
            res = []
            for key, value in objects.items():
                if value.amenity_id == Amenity.id:
                    res.append(value)
            return res

        @amenities.setter
        def amenities(self, obj):
            """Setter attr for adding Amenity.id"""
            if isinstance(obj, models.Amenity):
                self.amenity_ids.append(obj.id)
            else:
                pass
