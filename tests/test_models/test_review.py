#!/usr/bin/python3
""" Unittest for Review Class """
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestCity(unittest.TestCase):
    """ Test for Review """
    def setUp(self):
        """SetUp"""
        pass

    def test_class_attr(self):
        """Test to check attributes"""
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'text'))

    def test_attr_type(self):
        """Test for attr type"""
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.text, str)

    def test_inheritance(self):
        """Test to check inheritance from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))

    def tearDown(self):
        """TearDown"""
        pass
