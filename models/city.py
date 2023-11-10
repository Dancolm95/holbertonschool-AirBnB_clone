#!/usr/bin/python3
"""
Define the class 'City'.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ Define the name of city.

    Atributos:
        name(str): Name of the  city.
        state_id (str): Number of the State.
    """

    state_id = ""
    name = ""
