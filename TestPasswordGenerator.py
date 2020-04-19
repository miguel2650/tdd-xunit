import unittest
from PasswordGenerator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        # Instance of PasswordGenerator class
        passwordGen = PasswordGenerator()

        # Test cases for expected exceptions.
        testCases = [0.1, "string", None]
        # Tests that must fail
        for testcase in testCases:
            print("Expect exception with a", type(testcase))
            with self.assertRaises(Exception):
                passwordGen.length = testcase


if __name__ == "__main__":
    unittest.main()
