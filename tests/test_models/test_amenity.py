#!/usr/bin/python3
""" Unittest for Amenity Class """
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test for Amenity"""
    def setUp(self):
        """SetUp"""
        pass

    def test_class_attr(self):
        """Test to check attributes"""
        self.assertTrue(hasattr(Amenity, 'name'))
        self.assertIsInstance(Amenity.name, str)

    def test_inheritance(self):
        """Test to check inheritance from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def tearDown(self):
        """TearDown"""
        pass
