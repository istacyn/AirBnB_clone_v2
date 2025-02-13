#!/usr/bin/python3
"""This module instantiates object of class FileStorage"""
from os import environ
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review

if environ['HBNB_TYPE_STORAGE'] == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
