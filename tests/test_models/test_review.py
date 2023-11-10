#!/usr/bin/python3
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def test_attributes(self):
        """
        Verify that the attributes of Review are initialized correctly.
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_inheritance(self):
        """Verify that Review inherits from BaseModel."""
        review = Review()
        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == "__main__":
    unittest.main()
