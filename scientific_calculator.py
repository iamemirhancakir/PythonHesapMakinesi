import math
from cProfile import label      #burada hata aloyorum(I'm getting an error here and I can't figure it out.)
import matplotlib.pyplot as plt
import numpy as np


class ScientificCalculator:
    @staticmethod
    def sin(angle):
        """Derece cinsinden açı için sinüs hesaplar."""
        return math.sin(math.radians(angle))

    @staticmethod
    def cos(angle):
        """Derece cinsinden açı için kosinüs hesaplar."""
        return math.cos(math.radians(angle))

    @staticmethod
    def tan(angle):
        """Derece cinsinden açı için tanjant hesaplar."""
        return math.tan(math.radians(angle))

    @staticmethod
    def log(number, base=10):
        """Belirtilen tabanda logaritma hesaplar."""
        return math.log(number, base)

    @staticmethod
    def calculate_factorial():
        try:
            number = int(input("Faktoriyelini hesaplamak istediğiniz sayıyı girin: "))
            if number < 0:
                print("Negatif sayılar için faktoriyel hesaplanmaz.")
            else:
                print(f"{number}! = {math.factorial(number)}")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    @staticmethod
    def calculate_square_root():
        try:
            number = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
            if number < 0:
                print("Negatif sayıların karekökü hesaplanmaz.")
            else:
                print(f"Karekök{number} = {math.sqrt(number)}")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

    @staticmethod
    def plot_sine_wave():
        """Sinüs Grafiği Çizer."""
        x = np.linspace(0, 2 * np.pi, 500)
        y = np.sin(x)
        plt.plot(x,y, label="sin(x)",color = "blue")
        plt.title("Sinüs Grafiği")
        plt.xlabel("x")
        plt.ylabel("sin(x)")
        plt.legend()
        plt.grid()
        plt.show()

    @staticmethod
    def plot_cosine_wave():
        """Kosinüs grafiğini çizer."""
        x = np.linspace(0, 2 * np.pi, 500)
        y = np.cos(x)
        plt.plot(x,y, label = "cos(x)", color= "red")
        plt.title("Kosinüs Grafiği")
        plt.xlabel("x")
        plt.ylabel("cos(x)")
        plt.legend()
        plt.grid()
        plt.show()

    @staticmethod
    def plot_custom_function():
        """Kullanıcı tarafından tanımlanan bir fonksiyonun grafiğini çizer."""
        expression = input("Matematiksel ifadeyi girin örneğin: x**2: ")
        x = np.linspace(-10,10,500)
        try:
            y = eval(expression)
            plt.plot(x,y, label=f"{expression}", color = "green")
            plt.title(f"{expression} Grafiği")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.legend()
            plt.grid()
            plt.show()
        except Exception as e:
            print(f"Hata: Geçersiz ifade! ({e})")

