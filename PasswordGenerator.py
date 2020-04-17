class PasswordGenerator():

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

    def __str__(self):
        return str(self.length)


if __name__ == "__main__":
    print("Welcome to password generator")
    print("Answer the questions below to generate a new password")
    print("How long would you like your password to be?")
    inputLength = int(input())
    passwordGen = PasswordGenerator(inputLength)
    print('new password is ', passwordGen)
