class Checker:
    def checkExit(self, str):
        return str == "exit"

    def checkNumber(self, str):
        return str.isnumeric()

    def checkOption(self, str, idx):
        if self.checkNumber:
            return int(str) == idx
        else:
            return False
