class Calculator:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def division(a, b):
        return a / b

    @staticmethod
    def multiplation(a, b):
        return a * b


print("2 + 4 =", Calculator.addition(2, 4))
print("10 - 4 =", Calculator.subtraction(10, 4))
print("4 * 8 =", Calculator.multiplation(4, 8))
print("15 / 5 =", Calculator.division(15, 5))
