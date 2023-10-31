#!/usr/bin/bash
"""Define the Basemodel class"""


import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self)

    tform = "%Y-%m-%dT%H:%M:%S.%f"
    self.id = str(uuid4())
    self.created_at = datetime.today()
    self.updated_at = datetime.today()
    if len(kwargs) != 0:
        for k, v in kwargs.items():
            if k == "created_at" or k == "updated_at":
                self.__dict__[k] = datetime.strptime(v, tform)
            else:
                self.__dict__[k] = v
    else:
        models.storage.new(self)
