#!/usr/bin/python3
"""
Define the class 'User'.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represent a user.

    Attributes:
        email (str): user´s email.
        password (str): user's password.
        first_name (str): user's first name.
        last_name (str): user's second name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
