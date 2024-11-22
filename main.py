from calculator import Calculator
from conventer import Converter
from scientific_calculator import ScientificCalculator

def display_main_menu():
    print("\nAna Menü")
    print("1. Temel Hesaplama")
    print("2. Bilimsel Hesaplama")
    print("3. Birim Dönüştürme")
    print("0. Çıkış")

def scientific_calculator_menu():
    print("\nBilimsel Hesap Makinesi")
    print("1. Sinüs")
    print("2. Kosinüs")
    print("3. Tanjant")
    print("4. Logaritma")
    print("5. Faktoriyel")
    print("6. Karekök Hesaplama")
    print("7. Sinüs Grafiği Çizme")
    print("8. Kosinüs Grafiği Çizme")
    print("9. Kullanıcı Tanımlı Fonksiyon Grafiği")
    print("0. Ana Menü")

def unit_conversion_menu():
    print("\nBirim Dönüştürücü")
    print("1. Kilometre -> Mil")
    print("2. Mil -> Kilometre")
    print("3. Celsius -> Fahrenheit")
    print("4. Fahrenheit -> Celsius")
    print("5. Kilogram -> Pound")
    print("6. Pound -> Kilogram")
    print("7. Litre -> Galon")
    print("8. Galon -> Litre")
    print("9. Santimetre -> İnç")
    print("10. İnç -> Santimetre")
    print("0. Ana Menü")

def main():
    calc = Calculator()
    converter = Converter()
    sci_calc = ScientificCalculator()

    while True:
        display_main_menu()
        choice = input("Bir mod seçin (0-3): ")

        if choice == "0":
            print("Programdan çıkılıyor...")
            break

        elif choice == "1":
            # Temel hesaplama
            print("\nTemel Hesaplama")
            a = float(input("Birinci sayıyı girin: "))
            b = float(input("İkinci sayıyı girin: "))
            operation = input("İşlem türü seçin (+, -, *, /): ")

            if operation == "+":
                print(f"Sonuç: {calc.add(a, b)}")
            elif operation == "-":
                print(f"Sonuç: {calc.subtract(a, b)}")
            elif operation == "*":
                print(f"Sonuç: {calc.multiply(a, b)}")
            elif operation == "/":
                try:
                    print(f"Sonuç: {calc.divide(a, b)}")
                except ZeroDivisionError:
                    print("Hata: Sıfıra bölme yapılamaz!")
            else:
                print("Geçersiz işlem türü.")

        elif choice == "2":
            # Bilimsel hesaplama
            while True:
                scientific_calculator_menu()
                sci_choice = input("Bir işlem seçin (0-9): ")

                if sci_choice == "0":
                    break

                try:
                    if sci_choice == "1":
                        angle = float(input("Açıyı girin (derece): "))
                        print(f"Sinüs: {sci_calc.sin(angle):.2f}")
                    elif sci_choice == "2":
                        angle = float(input("Açıyı girin (derece): "))
                        print(f"Kosinüs: {sci_calc.cos(angle):.2f}")
                    elif sci_choice == "3":
                        angle = float(input("Açıyı girin (derece): "))
                        print(f"Tanjant: {sci_calc.tan(angle):.2f}")
                    elif sci_choice == "4":
                        number = float(input("Logaritması alınacak sayıyı girin: "))
                        base = float(input("Tabanı girin (Varsayılan: 10): ") or 10)
                        print(f"Logaritma: {sci_calc.log(number, base):.2f}")
                    elif sci_choice == "5":
                        sci_calc.calculate_factorial()
                    elif sci_choice == "6":
                        sci_calc.calculate_square_root()
                    elif sci_choice == "7":
                        sci_calc.plot_sine_wave()
                    elif sci_choice == "8":
                        sci_calc.plot_cosine_wave()
                    elif sci_choice == "9":
                        sci_calc.plot_custom_function()
                    else:
                        print("Geçersiz seçim.")
                except ValueError:
                    print("Lütfen geçerli bir sayı girin.")

        elif choice == "3":
            # Birim dönüştürme
            while True:
                unit_conversion_menu()
                unit_choice = input("Bir dönüşüm seçin (0-10): ")

                if unit_choice == "0":
                    break

                try:
                    if unit_choice == "1":
                        km = float(input("Kilometre girin: "))
                        print(f"Sonuç: {converter.km_to_miles(km):.2f} mil")
                    elif unit_choice == "2":
                        miles = float(input("Mil girin: "))
                        print(f"Sonuç: {converter.miles_to_km(miles):.2f} kilometre")
                    elif unit_choice == "3":
                        celsius = float(input("Celsius girin: "))
                        print(f"Sonuç: {converter.celsius_to_fahrenheit(celsius):.2f} Fahrenheit")
                    elif unit_choice == "4":
                        fahrenheit = float(input("Fahrenheit girin: "))
                        print(f"Sonuç: {converter.fahrenheit_to_celsius(fahrenheit):.2f} Celsius")
                    elif unit_choice == "5":
                        kg = float(input("Kilogram girin: "))
                        print(f"Sonuç: {converter.kg_to_pounds(kg):.2f} pound")
                    elif unit_choice == "6":
                        pounds = float(input("Pound girin: "))
                        print(f"Sonuç: {converter.pounds_to_kg(pounds):.2f} kilogram")
                    elif unit_choice == "7":
                        liters = float(input("Litre girin: "))
                        print(f"Sonuç: {converter.liters_to_gallons(liters):.2f} galon")
                    elif unit_choice == "8":
                        gallons = float(input("Galon girin: "))
                        print(f"Sonuç: {converter.gallons_to_liters(gallons):.2f} litre")
                    elif unit_choice == "9":
                        cm = float(input("Santimetre girin: "))
                        print(f"Sonuç: {converter.cm_to_inches(cm):.2f} inç")
                    elif unit_choice == "10":
                        inches = float(input("İnç girin: "))
                        print(f"Sonuç: {converter.inches_to_cm(inches):.2f} santimetre")
                    else:
                        print("Geçersiz seçim.")
                except ValueError:
                    print("Lütfen geçerli bir sayı girin.")
        else:
            print("Geçersiz seçim. Tekrar deneyin.")

if __name__ == "__main__":
    main()
