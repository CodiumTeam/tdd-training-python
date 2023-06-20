class RomanNumerals:

    def convert(self, decimal: int) -> str:
        if decimal == 8:
            return "V" + self.convert(decimal - 5)
        if decimal == 7:
            return "V" + self.convert(decimal - 5)
        if decimal == 6:
            return "V" + self.convert(decimal - 5)
        if decimal == 5:
            return "V" + self.convert(decimal - 5)
        if decimal == 4:
            return "IV"
        if decimal >= 1:
            return "I" + self.convert(decimal - 1)
        return ""
