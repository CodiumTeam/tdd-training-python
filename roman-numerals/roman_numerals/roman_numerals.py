class RomanNumerals:

    def convert(self, decimal: int) -> str:
        decimal_key = 5
        decimal_value = "V"
        if decimal >= decimal_key:
            return decimal_value + self.convert(decimal - decimal_key)
        if decimal >= 4:
            return "IV" + self.convert(decimal - 4)
        if decimal >= 1:
            return "I" + self.convert(decimal - 1)
        return ""
