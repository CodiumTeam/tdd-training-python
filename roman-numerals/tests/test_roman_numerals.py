import unittest

from parameterized import parameterized

from roman_numerals import RomanNumerals


class RomanNumeralsTest(unittest.TestCase):

    @parameterized.expand([
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (7, "VII"),
        (8, "VIII"),
    ])
    def test_convert_decimal_numbers(self, decimal: int, expected_roman: str):
        roman_numerals = RomanNumerals()

        roman = roman_numerals.convert(decimal)

        self.assertEqual(expected_roman, roman)