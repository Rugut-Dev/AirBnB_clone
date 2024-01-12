#!/usr/bin/python3
""" Unittest for Place Class """
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestCity(unittest.TestCase):
    """ Test for Place """
    def setUp(self):
        """SetUp"""
        pass

    def test_class_attr(self):
        """Test to check attributes"""
        self.assertTrue(hasattr(Place, 'name'))
        self.assertTrue(hasattr(Place, 'city_id'))
        self.assertTrue(hasattr(Place, 'user_id'))
        self.assertTrue(hasattr(Place, 'description'))
        self.assertTrue(hasattr(Place, 'number_rooms'))
        self.assertTrue(hasattr(Place, 'number_bathrooms'))
        self.assertTrue(hasattr(Place, 'max_guest'))
        self.assertTrue(hasattr(Place, 'price_by_night'))
        self.assertTrue(hasattr(Place, 'latitude'))
        self.assertTrue(hasattr(Place, 'longitude'))
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_attr_type(self):
        """ Test to check attr type """
        self.assertIsInstance(Place.name, str)
        self.assertIsInstance(Place.city_id, str)
        self.assertIsInstance(Place.user_id, str)
        self.assertIsInstance(Place.description, str)
        self.assertIsInstance(Place.number_rooms, int)
        self.assertIsInstance(Place.number_bathrooms, int)
        self.assertIsInstance(Place.max_guest, int)
        self.assertIsInstance(Place.price_by_night, int)
        self.assertIsInstance(Place.latitude, float)
        self.assertIsInstance(Place.longitude, float)
        self.assertIsInstance(Place.amenity_ids, list)

    def test_inheritance(self):
        """Test to check inheritance from BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))

    def tearDown(self):
        """TearDown"""
        pass
