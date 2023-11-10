#!/usr/bin/python3
"""
Define the class 'Place'.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Represent the place.

    Attributes:
        city_id (str): id of the  city.
        user_id (str): id of user.
        name (str): name of place.
        description (str): description of place .
        number_rooms (int): number of rooms.
        number_bathrooms (int): number of bathrooms.
        max_guest (int): max number of guests.
        price_by_night (int): the price by night.
        latitude (float): latitud of place.
        longitude (float): longitude of place.
        amenity_ids (list): list of services.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
