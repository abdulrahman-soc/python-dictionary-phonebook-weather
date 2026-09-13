# Python Dictionary — Phone Book & Weather Data

A practical Python project demonstrating dictionary-based data management through a phone book application and a weather data aggregation system.

The project was developed as part of a Python programming learning path, with an additional weather data feature implemented as a bonus to strengthen practical programming and data-handling skills relevant to cybersecurity automation.

---

## Overview

This project focuses on using Python dictionaries to store, retrieve, update, delete, and manage structured data.

It contains two independent programs:

1. **Phone Book** — A dictionary-based phone number lookup system.
2. **Weather Data Aggregation** — A nested dictionary system for managing weather information by city and date.

The weather application also includes input validation and CRUD-style operations for practical data management.

---

## Learning Objectives

This project demonstrates practical use of:

- Python dictionaries
- Nested dictionaries
- Key-value data structures
- Functions
- Conditional statements
- Loops
- Input handling
- Input validation
- Exception handling
- Data retrieval
- Data updating
- Data deletion
- Basic CRUD operations
- Structured data management

---

## Technologies

- Python 3
- Python Standard Library
- `datetime` module
- Git
- GitHub

---

## Project Structure

    python-dictionary-phonebook-weather/
    │
    ├── README.md
    ├── phone_book.py
    └── weather_data.py

---

## Features

### 1. Phone Book

The phone book program stores phone numbers as dictionary keys and owner names as values.

#### Functionality

- Accepts a phone number from the user.
- Validates that the number contains exactly 10 digits.
- Checks whether the number exists in the dictionary.
- Displays the owner's name when a match is found.
- Displays an appropriate message when the number does not exist.
- Rejects invalid input containing letters, symbols, or an incorrect number of digits.

#### Example

    Enter a phone number: 0568323222
    The name is: Amal

For a number that does not exist:

    Enter a phone number: 0500000000
    Sorry, the number is not found

For invalid input:

    Enter a phone number: 05683abc22
    This is invalid number

---

### 2. Weather Data Aggregation

The weather application uses a nested dictionary to organize weather information by city and date.

The data structure follows this concept:

    City
    └── Date
        ├── Temperature
        ├── Humidity
        └── Weather Condition

#### Example Data Structure

    weather_data = {
        "Riyadh": {
            "2026-09-13": {
                "temperature": 30,
                "humidity": 45,
                "condition": "Sunny"
            }
        }
    }

#### Functionality

- Add weather data.
- Search weather data by city and date.
- Update existing weather data.
- Delete weather data for a specific city and date.
- Display all stored weather data.
- Validate temperature input.
- Validate humidity values between 0 and 100.
- Validate date format using `YYYY-MM-DD`.
- Handle invalid user input.
- Prevent empty city names and weather conditions.

---

## Weather Application Menu

    ===== Weather Data Aggregation =====
    1. Add weather data
    2. Search weather data
    3. Update weather data
    4. Delete weather data
    5. Display all weather data
    6. Exit

---

## Input Validation

The weather application includes validation mechanisms to improve reliability and prevent invalid data from being stored.

### Temperature

Temperature must be entered as a numeric value.

    Enter temperature: 30

Invalid input such as:

    Enter temperature: abc

is rejected.

### Humidity

Humidity must be between 0 and 100 percent.

    Enter humidity (%): 45

Values outside this range are rejected.

### Date

Dates must follow the required format:

    YYYY-MM-DD

Example:

    2026-09-13

The application uses Python's `datetime.strptime()` to validate the date.

---

## CRUD Operations

The Weather Data Aggregation application implements basic CRUD-style data management:

| Operation | Description |
|---|---|
| Create | Add weather data |
| Read | Search and display weather data |
| Update | Modify existing weather data |
| Delete | Remove weather data |

This provides practical experience with managing structured data programmatically.

---

## Testing

The applications were tested using multiple scenarios.

### Phone Book Testing

- Valid existing phone number
- Valid non-existing phone number
- Invalid phone number containing letters
- Invalid phone number length

### Weather Testing

- Adding weather data
- Searching for existing weather data
- Updating weather data
- Verifying updated values
- Deleting weather data
- Verifying deleted data
- Displaying data when the dictionary is empty
- Invalid temperature input
- Invalid humidity input
- Invalid date input

---

## Example Weather Workflow

### Add

    City: Riyadh
    Date: 2026-09-13
    Temperature: 30
    Humidity: 45
    Condition: Sunny

### Update

The existing record can then be updated using the same city and date:

    City: Riyadh
    Date: 2026-09-13
    Temperature: 28
    Humidity: 40
    Condition: Cloudy

The city and date identify the existing record that should be modified.

---

## How to Run

Make sure Python 3 is installed.

### Run the Phone Book

Open a terminal in the project directory and run:

    python phone_book.py

### Run the Weather Application

    python weather_data.py

---

## Cybersecurity Relevance

Although this project focuses on Python fundamentals, the concepts demonstrated are directly useful in cybersecurity automation and SOC workflows.

Dictionaries and nested dictionaries are commonly useful for organizing and processing structured security data such as:

- IP address information
- IOC collections
- Alert metadata
- Security event attributes
- Incident records
- Log analysis results
- Threat intelligence data

Input validation and structured data handling are also important when developing reliable security automation scripts.

The project therefore provides a foundation for progressing toward more advanced Python-based cybersecurity automation.

---

## Skills Demonstrated

- Python Programming
- Dictionary Data Structures
- Nested Dictionaries
- Functions
- Loops
- Conditional Logic
- Input Validation
- Exception Handling
- Data Management
- CRUD Operations
- Problem Solving
- Basic Automation Concepts
- Cybersecurity Programming Fundamentals

---

## Future Improvements

Potential improvements for future versions include:

- Persisting weather data using JSON or a database.
- Adding multiple weather records for larger datasets.
- Adding sorting and filtering functionality.
- Adding statistical analysis of weather data.
- Adding logging functionality.
- Extending the project toward cybersecurity-focused data processing.
- Building a security log analysis application using similar dictionary-based structures.

---

## Author

**Abdulrahman**

Cybersecurity-focused learner developing practical programming and security automation skills.

GitHub: `abdulrahman-soc`

---

## License

This project was created for educational and portfolio purposes.
