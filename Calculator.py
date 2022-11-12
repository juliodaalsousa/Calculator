import math

class Calculator:
    def __init__(self):
        self.state = 0

    def setState(self, state):
        self.state = state

    def c(self):
        self.state = 0
        return self.state

    def sum(self, num):
        self.state += num
        return self.state
    def subtract(self, num):
        self.state -= num
        return self.state
    def multiplication(self, num):
        self.state *= num
        return self.state
    def division(self, num):
        self.state /= num
        return self.state

    def percent(self):
        self.state = self.state / 100
        return self.state

    def sqrt(self):
        self.state = math.sqrt(self.state)
        return self.state

    def pow2(self):
        self.state *= self.state
        return self.state
    def pow(self, num1, num2):
        res = 1;
        for i in range(num2):
            res = res * num1
        self.state = res
        return self.state


