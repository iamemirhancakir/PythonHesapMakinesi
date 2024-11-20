import math

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
