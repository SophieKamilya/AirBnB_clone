#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): The City id.
        idUser (str): The User id.
        name (str): The name of the place.
        descpt (str): The descpt of the place.
        roomNumber (int): The number of rooms of the place.
        bathroomsNumber (int): The number of bathrooms of the place.
        maxGuest (int): The maximum number of guests of the place.
        priceByNight(int): The price by night of the place.
        lati (float): The lati of the place.
        long (float): The long of the place.
        Amenity_ids (list): A list of Amenity ids.
    """

    city_id = ""
    roomNumber = 0
    bathroomsNumber = 0
    idUser = ""
    descpt = ""
    name = ""
    Amenity_ids = []
    maxGuest = 0
    lati = 0.0
    priceByNight= 0
    long = 0.0
