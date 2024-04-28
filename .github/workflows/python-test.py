name: Python CI

on:
  pull_request:
    branches: [ main ]  # Or whichever branches you want to run tests on

jobs:
  build:

    runs-on: ubuntu-latest

    strategy:
      matrix:
        python-version: [3.8, 3.9, 3.10]  # List any versions you want to test against

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        # List Custom Dependencies here:
    - name: Run tests
      run: |
        python -m unittest discover -s . -p "test_*.py"