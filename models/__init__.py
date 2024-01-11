#!/usr/bin/python3
"""initialize FileStorage"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
