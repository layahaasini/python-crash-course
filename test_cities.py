import unittest
from city_functions import format_place

class CityCountryTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do places like 'Athens' and 'Greece' work?"""
        formatted_place = format_place('athens', 'greece')
        self.assertEqual(formatted_place, 'Athens, Greece')

    def test_city_country_population(self):
        """Does input like 'Athens' , 'Greece' and '40000000' work?"""
        formatted_place = format_place('athens', 'greece', 40000000)
        self.assertEqual(formatted_place, 'Athens, Greece - Population 40000000')

unittest.main()