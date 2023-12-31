#!/usr/bin/python3
"""
test for BaseModel Class
"""
import unittest
from datetime import datetime
import models
import json

BaseModel = models.base_model.BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('.....  For BaseModel Class  .....')
        print('.................................\n\n')

    def test_doc_file(self):
        """documentation for the file"""
        expected = '\nBaseModel Class of Models Module\n'
        actual = models.base_model.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """documentation for the class"""
        expected = 'attributes and functions for BaseModel class'
        actual = BaseModel.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """documentation for init func"""
        expected = 'instantiation of new BaseModel Class'
        actual = BaseModel.__init__.__doc__
        self.assertEqual(expected, actual)

    def test_doc_save(self):
        """documentation for save func"""
        expected = 'updates attribute updated_at to current time'
        actual = BaseModel.save.__doc__
        self.assertEqual(expected, actual)

    def test_doc_to_json(self):
        """documentation for to_json func"""
        expected = 'returns json representation of self'
        actual = BaseModel.to_json.__doc__
        self.assertEqual(expected, actual)

    def test_doc_str(self):
        """documentation for to str func"""
        expected = 'returns string type representation of object instance'
        actual = BaseModel.__str__.__doc__
        self.assertEqual(expected, actual)


class TestBaseModelInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.....  For BaseModel Class  .....')
        print('.................................\n\n')

    def setUp(self):
        """initializes new BaseModel instance for testing"""
        self.model = BaseModel()

    def test_instantiation(self):
        """checks if BaseModel is properly instantiated"""
        self.assertIsInstance(self.model, BaseModel)

    def test_to_string(self):
        """checks if BaseModel is properly casted to str"""
        my_str = str(self.model)
        my_list = ['BaseModel', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """should not have updated attr"""
        my_str = str(self.model)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_save(self):
        """save func should add updated_at attr"""
        self.model.save()
        actual = type(self.model.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """to_json should return serializable dict object"""
        my_model_json = self.model.to_json()
        actual = 1
        try:
            serialized = json.dumps(my_model_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    def test_json_class(self):
        """to_json should include class key with value BaseModel"""
        my_model_json = self.model.to_json()
        actual = None
        if my_model_json['__class__']:
            actual = my_model_json['__class__']
        expected = 'BaseModel'
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """add name attr"""
        self.model.name = "Holberton"
        actual = self.model.name
        expected = "Holberton"
        self.assertEqual(expected, actual)

    def test_number_attribute(self):
        """add number attr"""
        self.model.number = 98
        actual = self.model.number
        self.assertTrue(98 == actual)

if __name__ == '__main__':
    unittest.main
