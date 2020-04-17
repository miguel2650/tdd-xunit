import unittest
import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        passwordGen = PasswordGenerator
        with self.assertRaises(Exception):
            passwordGen.length = "asd"


if __name__ == "__main__":
    unittest.main()
