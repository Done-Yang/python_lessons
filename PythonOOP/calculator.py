class SimpleCalculator():

    @staticmethod
    def add(num1, num2):
        resault = num1 + num2
        return ("{} + {} = {}".format(num1, num2, resault))

    @staticmethod
    def subtract(num1, num2):
        resault = num1 - num2
        return ("{} - {} = {}".format(num1, num2, resault))

    @staticmethod
    def multiply(num1, num2):
        resault = num1 * num2
        return ("{} * {} = {}".format(num1, num2, resault))

    @staticmethod
    def devide(num1, num2):
        resault = num1 / num2
        return ("{} / {} = {}".format(num1, num2, resault))
    
calculator = SimpleCalculator()


print(calculator.add(11, 21))
print(calculator.subtract(30, 20))
print(calculator.multiply(5, 3))
print(calculator.devide(12, 2))
