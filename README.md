# python-historical-dates

Python library for handling historical dates, including support for BCE dates. This library simplifies working with ancient and historical calendars without the complexities of modern datetime modules.

## Features

- Support for both BCE and CE dates.
- Simple and intuitive API for creating and manipulating historical dates.
- Functionality for comparing dates and calculating differences across eras.

## Installation

Install `python-historical-dates` via pip:

```bash
pip install historicaldates
```

## Quick Start

Here's how you can use python-historical-dates to create and manipulate historical dates:

```python
from historicaldates import HistoricalDate

# Create a historical date for January 1, 500 BCE
date_bce = HistoricalDate(-500, 1, 1)

# Create a historical date for December 31, 500 CE
date_ce = HistoricalDate(500, 12, 31)

# Calculate the number of days between two dates
days_between = date_ce - date_bce
print(f"Days between: {days_between}")
```

## How to Contribute

I welcome contributions from the community! Here are some ways you can contribute:
- Submit bugs and feature requests.
- Review the source code and improve documentation.
- Submit pull requests with bug fixes or new features.
Before contributing, please read the CONTRIBUTING.md file for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.