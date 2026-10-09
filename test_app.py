import unittest

from app import greet


class TestGreet(unittest.TestCase):
    def test_greet_with_name(self):
        self.assertEqual(greet("Python"), "Hello, Python!")

    def test_greet_defaults_to_world(self):
        self.assertEqual(greet(), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
