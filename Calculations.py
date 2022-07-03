class SimpleCalculations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

    def subtract(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            print("Error! The denominator cannot be 0")
        else:
            return self.a / self.b


class ComplexCalculations:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square(self):
        return self.a ** 2

    def cube(self):
        return self.a ** 3

    def power(self):
        return self.a ** self.b

    def sqr(self):
        return self.a ** (1. / 3)

    def cur(self):
        return self.a ** (1. / 3)

    def r(self):
        return self.a ** (1. / self.b)
