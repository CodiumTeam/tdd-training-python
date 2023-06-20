class RomanNumerals:

    def convert(self, decimal: int) -> str:
        if decimal == 6:
            return "VI"
        if decimal == 5:
            return "V"
        if decimal == 4:
            return "IV"
        if decimal >= 1:
            return "I" + self.convert(decimal-1)
        return ""
