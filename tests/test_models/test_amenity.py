#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def test_attributes(self):
        """
        Verify that the attributes of Amenity are initialized correctly.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertIsInstance(amenity.name, str)

    def test_inheritance(self):
        """Verify that Amenity inherits from BaseModel."""
        amenity = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()
