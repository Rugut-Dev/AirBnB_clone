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

    """
Test id's type if string
Test if id is unique
"""
    def test_id_type(self):
        base_model = BaseModel()
        base_model2 = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertNotEqual(base_model.id, base_model2.id)

    """Test for created_at time"""
    def test_created_at_is_current_datetime(self):
        with patch('models.base_model.datetime') as mock_datetime:
            fixed_time = datetime(2024, 1, 1, 1, 1, 1)
            mock_datetime.now.return_value = fixed_time
            base_model = BaseModel()
            self.assertIsInstance(base_model.created_at, datetime)
            self.assertEqual(base_model.created_at, fixed_time)

    def test_str_output(self):
        with patch('models.base_model.uuid') as mock_uuid,\
             patch('models.base_model.datetime') as mock_datetime:
            mock_uuid.uuid4.return_value =\
                uuid.UUID('123e4567-e89b-12d3-a456-426614174000')
            mock_datetime.now.return_value = datetime(2023, 1, 1, 1, 1, 1)

            base_model = BaseModel()
            expected_output = "[BaseModel] (123e4567-e89b-12d3-a456-426614174000) {'id': '123e4567-e89b-12d3-a456-426614174000', 'created_at': datetime.datetime(2023, 1, 1, 0, 0), 'updated_at': datetime.datetime(2023, 1, 1, 0, 0)}"

            self.assertEqual(str(base_model), expected_output)

    def tearDown(self):
        sys.stdout = sys.__stdout__
