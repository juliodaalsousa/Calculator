class Checker:
    def checkExit(self, str):
        return str == "exit"

    def checkNumber(self, str):
        if "-" in str:
            str = str.split("-")
            return str[1].isnumeric()
        else:
            return str.isnumeric()

    def checkDivision(self, num):
        return num == 0

    def checkSqrt(self, num):
        return num < 0

    def checkOption(self, str, idx):
        if self.checkNumber:
            return int(str) == idx
        else:
            return False
