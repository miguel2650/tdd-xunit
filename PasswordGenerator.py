class PasswordGenerator():

    # TODO: IF ALL IS FALSE WHAT IS PASSWORD? Length of X and contain ????
    def __init__(self, length=10, characters=True, numbers=True, specialChar=True, uppercase=True, lowercase=True):
        self.length = length
        self.characters = characters
        self.numbers = numbers
        self.specialChar = specialChar
        self.uppercase = uppercase
        self.lowercase = lowercase

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, len):
        if(type(len) is not int):
            raise Exception("Please use a number as length!")
        self._length = len

    @length.getter
    def length(self):
        return self._length

    # Function generate password based on user settings.
    def generatePassword(self):
        pass

    def __str__(self):
        return str(self.length)


if __name__ == "__main__":
    validInput = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    print("Welcome to password generator")
    print("Answer the questions below to generate a new password")
    print("How long would you like your password to be?")
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
    print("Contain lowercase letters:", passwordGen.lowercase)
