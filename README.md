# Calendar Application

This is a calendar application that displays holidays and the Chinese lunar calendar.

## Features

- Displays holidays for a given year.
- Converts Gregorian dates to lunar dates.

## Project Structure

```
pycalendar
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── holiday_calendar
│   │   ├── __init__.py
│   │   └── holidays.py
│   └── utils
│       ├── __init__.py
│       └── lunar_calendar.py
├── templates
│   └── index.html
├── static
│   └── styles.css
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/auding1900/pycalendar.git
   cd pycalendar
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Author

auding1900

## License

This project is licensed under the MIT License.
