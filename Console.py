from Checker import Checker

class Console:
    def __init__(self):
        self.checker = Checker()

    def welcome(self):
        print("Calculator : \n")
        print("Always you can type \"exit\" to go out of application \n")

    def read(self):
        text = input("> ")
        if self.checker.checkExit(text): exit()
        return text

    def readNumber(self):
        text = self.read()
        if not self.checker.checkNumber(text): return None
        return int(text)

    def verfyDivision(self, num):
        return self.checker.checkDivision(float(num))

    def verifySqrt(self, num):
        return self.checker.checkSqrt(float(num))

    def readOptions(self, options):
        text = self.read()
        for i in range(len(options)):
            if self.checker.checkOption(text, i): return int(text)
        return None

    def displayOptions(self, options):
        for i in range(len(options)):
            print(str(i) + " - " + options[i])



