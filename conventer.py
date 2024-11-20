class Converter:
    @staticmethod
    def km_to_miles(km):
        """Kilometreden mile dönüştür"""
        return km * 0.621371

    @staticmethod
    def miles_to_km(miles):
        """Milden kilometreye dönüştür"""
        return miles / 0.621371

    @staticmethod
    def celsius_to_fahrenheit(c):
        """Celsius'tan Fahrenheit'e dönüştür."""
        return (c * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        """Fahrenheit'ten Celsius'a dönüştür."""
        return (f - 32) * 5 / 9

    @staticmethod
    def kg_to_pounds(kg):
        """Kilogramdan pounda dönüştür."""
        return kg * 2.20462

    @staticmethod
    def pounds_to_kg(pounds):
        """Pounddan kilograma dönüştür."""
        return pounds / 2.20462

    @staticmethod
    def liters_to_gallons(liters):
        """Litreyi galona dönüştür."""
        return liters * 0.264172

    @staticmethod
    def gallons_to_liters(gallons):
        """Galonu litreye dönüştür."""
        return gallons / 0.264172

    @staticmethod
    def cm_to_inches(cm):
        """Santimetreyi inçe dönüştür."""
        return cm * 0.393701

    @staticmethod
    def inches_to_cm(inches):
        """İnçi santimetreye dönüştür."""
        return inches / 0.393701
