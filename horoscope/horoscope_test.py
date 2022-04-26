import unittest
import zodiac
from datetime import datetime


class TestHoroscope(unittest.TestCase):

    def test_format_date(self):
        print('Testing date_format')
        with self.assertRaises(ValueError):
            zodiac.format_date('2021-09-301')
            zodiac.format_date('0000-00-00')
            zodiac.format_date('29921-09-31')
            zodiac.format_date('202109301')
            zodiac.format_date('12/13/2022')
            zodiac.format_date('053091')


    def test_zodiac(self):
        print('Testing zodiac')
        formatted_date1 = zodiac.format_date('2021-09-30')
        formatted_date2 = zodiac.format_date('2021-12-01')
        formatted_date3 = zodiac.format_date('2021-01-01')
        formatted_date4 = zodiac.format_date('2000-03-28')
        formatted_date5 = zodiac.format_date('2015-05-31')
        self.assertEqual(zodiac.zodiac(formatted_date1), 'Libra')
        self.assertEqual(zodiac.zodiac(formatted_date2), 'Sagittarius')
        self.assertEqual(zodiac.zodiac(formatted_date3), 'Capricorn')
        self.assertEqual(zodiac.zodiac(formatted_date4), 'Aries')
        self.assertEqual(zodiac.zodiac(formatted_date5), 'Gemini')

    def test_check_name(self):
        print('Testing check_name')
        self.assertFalse(zodiac.check_name('!!!'))
        self.assertFalse(zodiac.check_name('.asd'))
        self.assertFalse(zodiac.check_name('_ania'))
        self.assertFalse(zodiac.check_name('*tomek*'))
        self.assertFalse(zodiac.check_name('Paulina1'))
        self.assertFalse(zodiac.check_name('Kamil-'))
        self.assertTrue(zodiac.check_name('ania'))
        self.assertTrue(zodiac.check_name('Ania'))

    def test_contains_number(self):
        print('Testing contains_number')
        self.assertFalse(zodiac.contains_number('Adam'))
        self.assertFalse(zodiac.contains_number('Andrew!'))
        self.assertFalse(zodiac.contains_number('__Nico__'))
        self.assertTrue(zodiac.contains_number('Adam1'))
        self.assertTrue(zodiac.contains_number('1Adrian'))

    def test_check_date(self):
        print('Testing check_date')
        formatted_date1 = zodiac.format_date('2021-01-01')
        formatted_date2 = zodiac.format_date('1999-09-05')
        formatted_date3 = zodiac.format_date('2023-01-01')
        formatted_date4 = zodiac.format_date('2555-12-15')
        formatted_date5 = zodiac.format_date('2022-12-30')
        self.assertTrue(zodiac.check_date(formatted_date1))
        self.assertTrue(zodiac.check_date(formatted_date2))
        self.assertFalse(zodiac.check_date(formatted_date3))
        self.assertFalse(zodiac.check_date(formatted_date4))
        self.assertFalse(zodiac.check_date(formatted_date5))


if __name__ == '__main__':
    unittest.main()