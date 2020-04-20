import unittest
from PasswordGenerator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    # Instance of PasswordGenerator class with default values
    # length=10, characters=True, numbers=True, specialChar=True, uppercase=True, lowercase=True
    passwordGen = PasswordGenerator()

    def test_constructor(self):
        self.assertIsInstance(self.passwordGen, PasswordGenerator)
        # TODO: More tests here?

    def test_length(self):

        # Test cases for expected exceptions.
        failTestCases = [-10, 0, 9, 31, "string", 0.1, None]
        for testcase in failTestCases:
            print("Expect exception with value:", testcase)
            with self.assertRaises(Exception):
                self.passwordGen.length = testcase

        # Test cases for expected success.
        successTestCases = [10, 15, 30]
        for testcase in successTestCases:
            print("Expect success with value:", testcase)
            self.passwordGen.length = testcase
            self.assertEqual(testcase, self.passwordGen.length)
            not self.assertRaises(Exception)

    def test_characters(self):

        # Test cases for expected exceptions.
        failTestCases = [1, "string", 0.1, None]
        for testcase in failTestCases:
            print("Expect exception with value:", testcase)
            with self.assertRaises(Exception):
                self.passwordGen.characters = testcase
                self.passwordGen.numbers = testcase
                self.passwordGen.specialChar = testcase
                self.passwordGen.uppercase = testcase
                self.passwordGen.lowercase = testcase

        # Test cases for expected success.
        successTestCases = [True, False]
        for testcase in successTestCases:
            print("Expect success with value:", testcase)
            self.passwordGen.characters = testcase
            self.assertEqual(testcase, self.passwordGen.characters)
            not self.assertRaises(Exception)

            self.passwordGen.numbers = testcase
            self.assertEqual(testcase, self.passwordGen.numbers)
            not self.assertRaises(Exception)

            self.passwordGen.specialChar = testcase
            self.assertEqual(testcase, self.passwordGen.specialChar)
            not self.assertRaises(Exception)

            self.passwordGen.uppercase = testcase
            self.assertEqual(testcase, self.passwordGen.uppercase)
            not self.assertRaises(Exception)

            self.passwordGen.lowercase = testcase
            self.assertEqual(testcase, self.passwordGen.lowercase)
            not self.assertRaises(Exception)

    def test_generatePassword(self):

        # Test cases
        testCases = [
            {
                "length": 10,
                "characters": True,
                "numbers": True,
                "specialChar": True,
                "uppercase": True,
                "lowercase": True
            },
            {
                "length": 30,
                "characters": False,
                "numbers": False,
                "specialChar": False,
                "uppercase": False,
                "lowercase": False
            },
            {
                "length": 15,
                "characters": False,
                "numbers": True,
                "specialChar": False,
                "uppercase": True,
                "lowercase": False
            },
            {
                "length": 15,
                "characters": True,
                "numbers": True,
                "specialChar": True,
                "uppercase": True,
                "lowercase": True
            }
        ]
        for testCase in testCases:
            self.passwordGen = PasswordGenerator(
                testCase['length'],
                testCase['characters'],
                testCase['numbers'],
                testCase['specialChar'],
                testCase['uppercase'],
                testCase['lowercase']
            )
            self.assertTrue(type(self.passwordGen.generatePassword()) is str)
            self.assertEqual(
                self.passwordGen.generatePassword().islower(), testCase['lowercase'])


'''        # Test cases for expected exceptions.
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
            self.assertEqual(testcase, passwordGen.length)'''


if __name__ == "__main__":
    unittest.main()
