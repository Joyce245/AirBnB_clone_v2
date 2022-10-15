#!/usr/bin/python3
"""Module for DBstorage"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Class for save in DB"""

    __engine = None
    __session = None

    def __init__(self):
        """The init return the instance"""

        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        LH = os.getenv('HBNB_MYSQL_HOST')
        DB = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, LH, DB),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == "test":
            Base.metada.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the database session and output a dict"""

        dicty = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                dicty[key] = obj
        else:
            objects = [State, City, User, Place, Review, Amenity]
            for clas in objects:
                query = self.__session.query(clas)
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    dicty[key] = obj
        return dicty

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """close the session"""
        self.__session.close()
