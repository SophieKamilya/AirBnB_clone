#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.crea_at = datetime.today()
        self.upd_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "crea_at" or k == "upd_at":
                    self.__dict__[k] = datetime.strptime(v, time_form)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update upd_at with the current datetime."""
        self.upd_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["crea_at"] = self.crea_at.isoformat()
        rdict["upd_at"] = self.upd_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)
