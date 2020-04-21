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
        
        return ''.join([password[randint(0, len(password)-1)] for i in range(self.length)])

    def __str__(self):
        return str(self.length)


if __name__ == "__main__":
    pass
'''    validInput = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    print("Welcome to password generator")
    print("Answer the questions below to generate a new password")
    print("How long would you like your password to be? (minimum 10, maximum 30)")
    inputLength = int(input())
    print("Would you like your password to contain characters? yes/no")
    inputCharacters = str(input())
    if(inputCharacters.lower() not in validInput):
        raise ValueError("Invalid answer")
    print("Would you like your password to contain numbers? yes/no")
    inputNumbers = str(input())
    if(inputNumbers.lower() not in validInput):
        raise ValueError("Invalid answer")
    print("Would you like your password to contain special characters? yes/no")
    inputSpecialChar = str(input())
    if(inputSpecialChar.lower() not in validInput):
        raise ValueError("Invalid answer")
    print("Would you like your password to contain uppercase letters? yes/no")
    inputUppercase = str(input())
    if(inputUppercase.lower() not in validInput):
        raise ValueError("Invalid answer")
    print("Would you like your password to contain lowercase letters? yes/no")
    inputLowercase = str(input())
    if(inputLowercase.lower() not in validInput):
        raise ValueError("Invalid answer")

    passwordGen = PasswordGenerator(
        inputLength, validInput[inputCharacters.lower()], validInput[inputNumbers.lower()], validInput[inputSpecialChar.lower()], validInput[inputUppercase.lower()], validInput[inputLowercase.lower()])

    print('Success: Your new password will be created with following settings...')
    print("Password length:", passwordGen.length)
    print("Contain characters:", passwordGen.characters)
    print("Contain numbers:", passwordGen.numbers)
    print("Contain special characters:", passwordGen.specialChar)
    print("Contain uppercase letters:", passwordGen.uppercase)
    print("Contain lowercase letters:", passwordGen.lowercase)'''
