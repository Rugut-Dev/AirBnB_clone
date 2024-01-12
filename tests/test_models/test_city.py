#!/usr/bin/python3
""" Unittest for City Class """
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Test for State """
    def setUp(self):
        """SetUp"""
        pass

    def test_class_attr(self):
        """Test to check attributes"""
        self.assertTrue(hasattr(City, 'name'))
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertIsInstance(City.name, str)
        self.assertIsInstance(City.state_id, str)

    def test_inheritance(self):
        """Test to check inheritance from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def tearDown(self):
        """TearDown"""
        pass
