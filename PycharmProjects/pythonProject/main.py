import print_name as print_name


class Calculator:
    def add(num1, num2):
        return num1 + num2

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        return num1 / num2

Calculator.add = staticmethod(Calculator.add)

print("1 + 1 =", Calculator.add(1, 1))
print("2 * 2 =", Calculator.multiply(2, 2))
print("100 / 2 =", Calculator.divide(100, 2))


class Utilities:

    @staticmethod
    def print_name(self):
        return "Electricity"

    @staticmethod
    def print_name2(self):
        return "Water Board"

    @staticmethod
    def print_name3(self):
        return "Gas"

printName = staticmethod(print_name)
print("Utility1 =", Utilities.print_name("Electricity"))
print("Utility2 =", Utilities.print_name2("Water Board"))
print("Utility3 =", Utilities.print_name3("Gas"))