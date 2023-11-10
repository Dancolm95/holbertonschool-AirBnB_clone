#!/usr/bin/python3
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def test_attributes(self):
        """
        Verify that the atrributes of State initialized correctly.
        """
        state = State()
        self.assertEqual(state.name, "")
        self.assertIsInstance(state.name, str)

    def test_inheritance(self):
        """Verify that State inherits from BaseModel."""
        state = State()
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == "__main__":
    unittest.main()
