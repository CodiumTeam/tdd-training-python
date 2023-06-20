class RomanNumerals:

    def convert(self, decimal: int) -> str:
        conversion = {
            5: "V",
            4: "IV",
        }
        for decimal_key in conversion.keys():
            decimal_value = conversion.get(decimal_key)
            if decimal >= decimal_key:
                return decimal_value + self.convert(decimal - decimal_key)
        if decimal >= 1:
            return "I" + self.convert(decimal - 1)
        return ""
