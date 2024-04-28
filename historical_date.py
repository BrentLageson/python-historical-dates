"""
This module provides the HistoricalDate class to handle dates in both BCE and CE formats.
"""

# Imports
import calendar

# Classes
class HistoricalDate:
    """
    Represents a date in history, supporting both BCE and CE dates.

    Attributes:
        year (int): The year of the date, negative for BCE and positive for CE.
        month (int): The month of the date, ranging from 1 (January) to 12 (December).
        day (int): The day of the month, ranging from 1 to 31 based on the month.

    Methods:
        add_years(self, years): Adds or subtracts years from the date, adjusting the BCE/CE setting as needed.
    """
    def __init__(self, year, month, day):
        if year == 0:
            raise ValueError("Year must be non-zero")
        if not 1 <= month <= 12:
            raise ValueError("Month must be between 1 and 12")
        if not 1 <= day <= 31:
            raise ValueError("Day must be between 1 and 31")
        if day > calendar.monthrange(year if year >= 0 else year - 1, month)[1]:
            raise ValueError("Invalid day for the given month and year")
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        era = "BCE" if self.year < 0 else "CE"
        year_str = str(abs(self.year))
        return f"{self.month}/{self.day}/{year_str} {era}"

    def __eq__(self, other):
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def add_years(self, years):
        self.year += years

    # Add more methods here:
