#!/usr/bin/python3
"""Holds reviews"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Managed Review objects"""
    place_id = ""
    user_id = ""
    text = ""