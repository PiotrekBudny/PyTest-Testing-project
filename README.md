# PyTest-Testing-Project

This project demonstrates **API**, **unit**, and **end-to-end (E2E) UI testing** in Python using [pytest](https://pytest.org/), [requests](https://docs.python-requests.org/), and [Selenium WebDriver](https://www.selenium.dev/).  
It follows best practices such as the **Page Object Model** for UI tests, uses assertion helper classes for clean, maintainable code, and includes realistic simulation and exception handling for unit tests.

## Features

- **API Testing**
  - Uses `requests` and `pytest` to test the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) fake REST API.
  - Includes tests for GET, POST, and error scenarios.
  - Assertion helpers for validating API responses.

- **Unit Testing**
  - Tests for core logic, such as a simulated `Multimeter` and `Battery` components.
  - Uses fixtures to set up test data and objects.
  - Custom exceptions and assertion helpers for domain-specific checks.
  - Simulates realistic measurement values.
  - Tests for mocked api handler when lotto api responses are fake.

- **E2E UI Testing**
  - Uses Selenium WebDriver and pytest for browser automation.
  - Implements the Page Object Model for maintainable UI tests.
  - Supports headless browser mode for CI and local runs.
  - Example tests for login, logout, and error handling.

## Project Structure

```
api/
  test_api.py           # API test cases
  api_route_builder.py   # Helper for building API URLs
  models/                # Data models for requests/responses
  api_assertions.py      # Assertion helpers for API responses

e2e/
  test_e2e.py            # E2E UI test cases
  pages/                 # Page Object Model classes
  assertions/            # Assertion helpers for UI tests

unittests/
  multimeter/            # Multimeter logic, components, and utils
    test_multimeter.py   # Unit tests for multimeter and battery
  mockedapi/             # Mocked lotto api logic, utils
    test_mockedapi.py    # Unit tests for mocked lotto api handler

api_variables.py         # Configuration (API base URL, login credentials, etc.)
e2e_variables.py         # Configuration for E2E tests (login URL, credentials, headless mode)
requirements.txt         # Project dependencies
```

## Getting Started

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Run all tests:**
   ```
   pytest
   ```

3. **Run API tests only:**
   ```
   pytest api/
   ```

4. **Run E2E tests (headless by default):**
   ```
   pytest e2e/
   ```
   > For E2E tests, make sure you have [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed and available in your PATH.

5. **Run Unit tests:**
   ```
   pytest unittests/
   ```

## Customization

- Update `api_variables.py` and `e2e_variables.py` with your API base URL, test credentials, and E2E settings as needed.
- Add or modify Page Object classes in `e2e/pages/` for your application’s UI.
- Extend unit tests and components in `unittests/multimeter/` and `unittests/mockedapi/` as your logic grows.

## Continuous Integration

You can use GitHub Actions for free CI. Add this workflow to `.github/workflows/python-tests.yml`:

```yaml
name: Python package

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.12'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run all tests
      run: pytest -v
```
