#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        idPlace (str): The Place id.
        idUser (str): The User id.
        text (str): The text of the review.
    """

    idPlace = ""
    idUser = ""
    text = ""
