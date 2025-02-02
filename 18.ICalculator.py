'''18. Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, 
`multiply()`, and `divide()`.
 Create a `BasicCalculator` class that implements these methods.'''
 
from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass

    @abstractmethod
    def multiply(self):
        pass

    @abstractmethod
    def divide(self):
        pass

class BasicCalculator(ICalculator):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2
    
basic_calc = BasicCalculator(int(input("Enter the first number: ")), int(input("Enter the second number: ")))
print(f"Addition: {basic_calc.add()}")
print(f"Subtraction: {basic_calc.subtract()}")
print(f"Multiplication: {basic_calc.multiply()}")
print(f"Division: {basic_calc.divide()}")