import math

class Calculator:
    def __init__(self):
        pass

    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a - b
    def multiply(self,a,b):
        return a * b
    def divide(self,a,b):
        if b == 0:
            raise ValueError("Sıfıra bölünmez")
        return a / b

    def power(self,a,b):
        return math.pow(a,b)

    def sqrt(self,a):
        if a < 0:
            raise ValueError("Negatif sayının karekökü olamaz")
        return math.sqrt(a)




