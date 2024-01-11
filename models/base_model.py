#!/usr/bin/python3
""" Defines all common attributes/methods for other classes"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class defining attrs and methods for the whole project"""
    def __init__(self, *args, **kwargs):
        """initilizes public instances id, created_at, updated_at attributes"""
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']
            for key, val in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):

        """return a friendly string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
Updates the public instance attribute 'updated_at' with the current datetime
"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dict object"""
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()

        return dict_obj
