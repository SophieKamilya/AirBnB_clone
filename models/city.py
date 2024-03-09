#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Attributes:
        stat_id (str): The state id.
        name (str): The name of the city.
    """

    stat_id = ""
    name = ""
