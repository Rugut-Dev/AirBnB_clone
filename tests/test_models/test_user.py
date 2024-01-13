#!/usr/bin/python3
"""Contains the unittests for the class User"""
from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """Contains test cases for User class"""
    def setUp(self):
        """setup"""
        pass

    def test_inheritance(self):
        """Tests if user inherits BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_public_cls_attrs(self):
        """Tests the public class attributes"""
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_attrs_type(self):
        """Tests the type of attr(str)"""
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.last_name, str)
        self.assertIsInstance(User.first_name, str)

    def tearDown(self):
        pass
