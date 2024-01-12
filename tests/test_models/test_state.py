#!/usr/bin/python3
""" Unittest for State Class """
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Test for State"""
    def setUp(self):
        """SetUp"""
        pass

    def test_class_attr(self):
        """Test to check attributes"""
        self.assertTrue(hasattr(State, 'name'))
        self.assertIsInstance(State.name, str)

    def test_inheritance(self):
        """Test to check inheritance from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def tearDown(self):
        """TearDown"""
        pass
