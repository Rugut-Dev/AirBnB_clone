#!/usr/bin/python3
"""Responsible for the city location"""
from models.base_model import BaseModel


class City(BaseModel):
    """Manages city objects"""
    state_id = ""
    name = ""
