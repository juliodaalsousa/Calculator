from Console import Console
from Calculator import Calculator

class App:
    def __init__(self):
        self.console = Console()
        self.calculator = Calculator()
        self.collec = ["Give a initial state", "Sum", "Clear", "Subtract", "Multiplication", "Division", "Percent", "Square root", "Power by 2", "Power"]

    def start(self):
        self.console.welcome()
        self.display()

    def display(self):
        self.console.displayOptions(self.collec)
        print("Your result => " + str(self.calculator.state))
        res = self.__askOption("Select an option ")
        if res == 0:
            print("Type a number")
            num = self.console.readNumber()
            self.calculator.setState(num)
            self.display()
        elif res == 1:
            print("Type a number")
            num = self.console.readNumber()
            self.calculator.sum(num)
            self.display()
        elif res == 2:
            self.calculator.c()
            self.display()
        elif res == 3:
            print("Type a number")
            num = self.console.readNumber()
            self.calculator.subtract(num)
            self.display()
        elif res == 4:
            print("Type a number")
            num = self.console.readNumber()
            self.calculator.multiplication(num)
            self.display()
        elif res == 5:
            print("Type a number")
            num = self.console.readNumber()
            self.calculator.division(num)
            self.display()
        elif res == 6:
            self.calculator.percent()
            self.display()
        elif res == 7:
            self.calculator.sqrt()
            self.display()
        elif res == 8:
            self.calculator.pow2()
            self.display()
        elif res == 9:
            print("Type a number (first)")
            num1 = self.console.readNumber()
            print("Type a number (second)")
            num2 = self.console.readNumber()
            self.calculator.pow(num1, num2)
            self.display()


    def __askOption(self, title):
        while True:
            print(title)
            text = self.console.readOptions(self.collec)
            if text != None:
                return int(text)