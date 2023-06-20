class RomanNumerals:

    def convert(self, decimal: int) -> str:
        if decimal == 1:
            return "I" + ""
        if decimal == 2:
            return "I" + "I"
        if decimal == 3:
            return "I" + "II"
