#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes: name: input name
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")

    else:
        @property
        def cities(self):
            """returns the list of City instances with
            state_id equals to the current State.id
            """
            objects = models.storage.all(City)
            my_list = []

            for city_id, city_obj in objects.items():
                if city_obj.state_id == self.id:
                    my_list.append(city_obj)

            return my_list
