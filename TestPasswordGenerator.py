import unittest
from PasswordGenerator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        # Instance of PasswordGenerator class
        passwordGen = PasswordGenerator()

        # Tests that must fail
        with self.assertRaises(Exception):
            passwordGen.length = "i am a string"


if __name__ == "__main__":
    unittest.main()
