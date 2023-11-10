#!/usr/bin/python3
"""
Define the class 'Review'.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): id of place.
        user_id (str): id of user.
        text (str): text of review.
    """

    place_id = ""
    user_id = ""
    text = ""
