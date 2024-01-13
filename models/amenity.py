#!/usr/bin/python3
"""Class inheriting from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Manages amenity objects"""
    name = ""
