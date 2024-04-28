"""
This module contains unittests for the HistoricalDate class.
"""

# Imports
import unittest
from historical_date import HistoricalDate

# Classes
class TestHistoricalDate(unittest.TestCase):
    """
    Test suite for the HistoricalDate class.

    This class tests the correct initialization of dates, 
    ensuring that invalid dates raise appropriate errors.
    """
    def test_date_creation(self):
        """
        Test the creation of HistoricalDate objects
        """
        # Test valid date creation
        date = HistoricalDate(2023, 4, 28)
        self.assertEqual((date.year, date.month, date.day), (2023, 4, 28))

        # Test BCE date creation
        date_bce = HistoricalDate(-500, 1, 1)
        self.assertEqual((date_bce.year, date_bce.month, date_bce.day), (-500, 1, 1))

    def test_invalid_date_creation(self):
        """
        Test the creation of invalid HistoricalDate objects
        """
        # Test invalid month
        with self.assertRaisesRegex(ValueError, "Month must be between 1 and 12"):
            HistoricalDate(2023, 13, 1)

        # Test invalid day
        with self.assertRaisesRegex(ValueError, "Invalid day for the given month and year"):
            HistoricalDate(2023, 2, 30)

        # Testing negative or zero year
        with self.assertRaisesRegex(ValueError, "Year must be non-zero"):
            HistoricalDate(0, 1, 1)

        # Test creating a date with a day too large for the month
        with self.assertRaisesRegex(ValueError, "Invalid day for the given month and year"):
            HistoricalDate(2023, 4, 31)  # April has 30 days

    def test_date_comparison(self):
        """
        Test the comparison of HistoricalDate objects
        """
        date1 = HistoricalDate(2023, 4, 28)
        date2 = HistoricalDate(2023, 4, 28)
        date3 = HistoricalDate(2022, 4, 28)
        self.assertTrue(date1 == date2)
        self.assertTrue(date1 != date3)

    def test_add_years(self):
        """
        Test addition of years to HistoricalDate objects
        """
        date = HistoricalDate(2020, 1, 1)
        date.add_years(5)
        self.assertEqual((date.year, date.month, date.day), (2025, 1, 1))

        # Testing BCE to CE transition
        date_bce = HistoricalDate(-1, 12, 31)
        date_bce.add_years(2)
        self.assertEqual((date_bce.year, date_bce.month, date_bce.day), (1, 12, 31))

    def test_str(self):
        """
        Test object str
        """
        date = HistoricalDate(2023, 4, 28)
        self.assertEqual(str(date), "4/28/2023 CE")

        date_bce = HistoricalDate(-2023, 4, 28)
        self.assertEqual(str(date_bce), "4/28/2023 BCE")

if __name__ == '__main__':
    unittest.main()
