#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
import MySQLdb
from unittest.mock import patch


unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "NO apply for db")


class TestDBStorage(unittest.TestCase):
    """This will test the DBStorage"""
    def testPep8(self):
        """test for pep8 style"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         'Found code style errors (and warnings).')

    @classmethod
    def setUpClass(self):
        """run method priot test"""
        self.storage = DBStorage()

    def testState(self):
        state = State(name='California')
        self.assertEqual(state.name, 'California')
