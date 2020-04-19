import unittest
from PasswordGenerator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    def test_length(self):
        # Instance of PasswordGenerator class with default values
        # length=10, characters=True, numbers=True, specialChar=True, uppercase=True, lowercase=True
        passwordGen = PasswordGenerator()

        # Test cases for expected exceptions.
        failTestCases = [0.1, "string", None]
        for testcase in failTestCases:
            print("Expect exception with a", type(testcase))
            with self.assertRaises(Exception):
                passwordGen.length = testcase

        # Test cases for expected success.
        successTestCases = [-1000, -1, 0, 1, 1000]
        for testcase in successTestCases:
            print("Expect success with ", testcase)
            passwordGen.length = testcase
            self.assertEqual(testcase, passwordGen.length)


if __name__ == "__main__":
    unittest.main()
