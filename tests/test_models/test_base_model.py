#!/usr/bin/python3
"""Unit test for BaseModel Class"""
import unittest
from unittest.mock import patch
from datetime import datetime, timedelta
from models.base_model import BaseModel
import sys
from io import StringIO
import uuid


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output

    """Test cases for BaseModel classes"""
    def test_public_inst_attrs(self):
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))

    
    def test_id_type(self):
        """
        Test id's type if string
        Test if id is unique
        """
        base_model = BaseModel()
        base_model2 = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertNotEqual(base_model.id, base_model2.id)

    def test_public_inst_attrs(self):
        """
        Tests if public instance attrs
        Tests if public instance methods
        """
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertAlmostEqual(base_model.created_at, datetime.now(), delta=timedelta(microseconds=100))
        self.assertTrue(hasattr(base_model, 'updated_at'))
        self.assertAlmostEqual(base_model.updated_at, datetime.now(), delta=timedelta(microseconds=100))
        self.assertTrue(hasattr(base_model, 'save'))
        self.assertTrue(hasattr(base_model, 'to_dict'))

    def test_str_output(self):
        """Tests for the output of _str_"""
        base_model = BaseModel()
        expected_output = f"[{base_model.__class__.__name__}] ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_output)
    
    def test_save_method(self):
        """Tests the functionality of save method"""
        base_model = BaseModel()
        d1 = base_model.updated_at
        base_model.save()
        d2 = base_model.updated_at
        self.assertNotEqual(d2, d1)
    
    def test_to_dict_method(self):
        """Tests the to_dict output"""
        base_model = BaseModel()
        base_model.created_at = datetime(2022, 1, 1, 12, 0, 0, 0)
        base_model.updated_at = datetime(2022, 1, 2, 12, 0, 0, 0)

        result_dict = base_model.to_dict()

        self.assertIn('__class__', result_dict)
        self.assertEqual(result_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', result_dict)
        self.assertIn('updated_at', result_dict)
        
        for key, value in base_model.__dict__.items():
            if key not in ['created_at', 'updated_at']:
                self.assertIn(key, result_dict)
                self.assertEqual(result_dict[key], value)

        expected_created_at = base_model.created_at.isoformat().split('.')[0]
        expected_updated_at = base_model.updated_at.isoformat().split('.')[0]
        self.assertEqual(result_dict['created_at'], expected_created_at)
        self.assertEqual(result_dict['updated_at'], expected_updated_at)

    def tearDown(self):
        sys.stdout = sys.__stdout__
