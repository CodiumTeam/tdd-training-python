class RomanNumerals:

    def convert(self, decimal: int) -> str:
        if decimal == 1:
            return "I"
        if decimal == 2:
            return "II"
        if decimal == 3:
            return "III"
