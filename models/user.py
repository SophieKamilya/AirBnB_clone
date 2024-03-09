#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attributes:
        usrEmail (str): The usrEmail of the user.
        usrPassword (str): The usrPassword of the user.
        firstName (str): The first name of the user.
        lastName (str): The last name of the user.
    """

    usrEmail = ""
    usrPassword = ""
    firstName = ""
    lastName = ""
