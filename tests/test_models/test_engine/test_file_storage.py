#!/usr/bin/python3
"""Contains Test cases for the file storage class"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import sys
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = 'file.json'
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def test_all_method9(self):
        """Tests all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_method(self):
        """Tests the new method of FileStorage"""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.assertIn('BaseModel.' + base_model.id,
                      self.storage.all())

    def test_save_and_reload_methods(self):
        """Test the save and reload methods of FileStorage"""
        base_model = BaseModel()
        self.storage.new(base_model)
        self.storage.save()

        self.assertTrue(os.path.exists(self.file_path))

        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        key = '{}.{}'.format(base_model.__class__.__name__, base_model.id)
        self.assertIn(key, new_storage.all())

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
