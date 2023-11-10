#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def test_attributes(self):
        """
        Verify that the attributes of City are initialized correctly.
        """
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")
        self.assertIsInstance(city.name, str)
        self.assertIsInstance(city.state_id, str)

    def test_inheritance(self):
        """Verify that City inherits from BaseModel."""
        city = City()
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == "__main__":
    unittest.main()
