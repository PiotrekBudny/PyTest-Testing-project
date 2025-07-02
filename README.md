# PyTest-Testing-Project

This project demonstrates **API** and **end-to-end (E2E) UI testing** in Python using [pytest](https://pytest.org/), [requests](https://docs.python-requests.org/), and [Selenium WebDriver](https://www.selenium.dev/).  
It follows best practices such as the **Page Object Model** for UI tests and uses assertion helper classes for clean, maintainable code.

## Features

- **API Testing**
  - Uses `requests` and `pytest` to test the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) fake REST API.
  - Includes tests for GET, POST, and error scenarios.
  - Assertion helpers for validating API responses.

- **E2E UI Testing**
  - Uses Selenium WebDriver and pytest for browser automation.
  - Implements the Page Object Model for maintainable UI tests.
  - Example tests for login, logout, and error handling.

## Project Structure

```
api/
  api_tests.py           # API test cases
  api_route_builder.py   # Helper for building API URLs
  models/                # Data models for requests/responses
  api_assertions.py      # Assertion helpers for API responses

e2e/
  e2e_tests.py           # E2E UI test cases
  pages/                 # Page Object Model classes
  assertions/            # Assertion helpers for UI tests

variables.py             # Configuration (API base URL, login credentials, etc.)
```

## Getting Started

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Run API tests:**
   ```
   pytest api/api_tests.py
   ```

3. **Run E2E tests:**
   ```
   pytest e2e/e2e_tests.py
   ```
   > For E2E tests, make sure you have [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed and available in your PATH.

## Customization

- Update `variables.py` with your API base URL and test credentials as needed.
- Add or modify Page Object classes in `e2e/pages/` for your application’s UI.

##