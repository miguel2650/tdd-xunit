from random import randint
import string


class PasswordGenerator():

    # TODO: IF ALL IS FALSE WHAT IS PASSWORD? Length of X and contain ????
    def __init__(self, length=10, characters=True, numbers=True, specialChar=True, uppercase=True, lowercase=True):
        self.length = self.validateLength(length)
        self.characters = self.validateBoolean(characters)
        self.numbers = self.validateBoolean(numbers)
        self.specialChar = self.validateBoolean(specialChar)
        self.uppercase = self.validateBoolean(uppercase)
        self.lowercase = self.validateBoolean(lowercase)

    # Can act as a getter function
    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, len):
        self._length = self.validateLength(len)

    @property
    def characters(self):
        return self._characters

    @characters.setter
    def characters(self, char):
        self._characters = self.validateBoolean(char)

    @property
    def numbers(self):
        return self._numbers

    @numbers.setter
    def numbers(self, num):
        self._numbers = self.validateBoolean(num)

    @property
    def specialChar(self):
        return self._specialchar

    @specialChar.setter
    def specialChar(self, sChar):
        self._specialchar = self.validateBoolean(sChar)

    @property
    def uppercase(self):
        return self._uppercase

    @uppercase.setter
    def uppercase(self, upCase):
        self._uppercase = self.validateBoolean(upCase)

    @property
    def lowercase(self):
        return self._lowercase

    @lowercase.setter
    def lowercase(self, lowCase):
        self._lowercase = self.validateBoolean(lowCase)

    def validateLength(self, len):
        if(not type(len) is int):
            raise TypeError("Expected int")
        if(len < 10 or len > 30):
            raise ValueError("Out of boundary exception")
        return len

    def validateBoolean(self, input):
        if(not type(input) is bool):
            raise TypeError("Expected boolean")
        return input

    # Function generate password based on user settings.
    def generatePassword(self):
        password = ''
        if self.characters:
            password += string.ascii_lowercase + string.ascii_uppercase
        if self.numbers:
            password += string.digits
        if self.specialChar:
            password += string.punctuation
        if self.uppercase and not self.lowercase:
            password = password.upper()
        if self.lowercase and not self.uppercase:
            password = password.lower()
        try:
            return ''.join([password[randint(0, len(password)-1)] for i in range(self.length)])
        except ValueError:
            raise Exception('Password should contain at least characters, special characters or numbers.')

    def __str__(self):
        return str(self.length)