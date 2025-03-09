from flask import Flask, render_template, request
from holiday_calendar.holidays import HolidayManager
from utils.lunar_calendar import LunarCalendar
import datetime
import calendar

app = Flask(__name__)

@app.template_filter('zip')
def zip_filter(a, b):
    return zip(a, b)

app.jinja_env.filters['zip'] = zip_filter

@app.route("/", methods=["GET", "POST"])
def index():
    today = datetime.date.today()
    year = today.year
    month = today.month

    if request.method == "POST":
        year = int(request.form.get("current_year", today.year))
        month = int(request.form.get("current_month", today.month))

        if "prev" in request.form:
            month -= 1
            if month == 0:
                month = 12
                year -= 1
        elif "next" in request.form:
            month += 1
            
            if month == 13:
                month = 1
                year += 1
        elif "today" in request.form:
            year = today.year
            month = today.month
        elif "any" in request.form:
            year = int(request.form["year"])
            month = int(request.form["month"])

    holiday_manager = HolidayManager(countries=['US', 'JP', 'CN'])  # Add desired countries here
    holidays = holiday_manager.get_holidays(year, month)
    # print(f"Holidays for {year}-{month}: {holidays}")  # Debug print

    lunar_calendar = LunarCalendar()
    lunar_dates = lunar_calendar.get_lunar_dates(year, month)
    # print(f"Lunar dates for {year}-{month}: {lunar_dates}")  # Debug print

    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)
    # print(f"Calendar for {year}-{month}: {month_days}")  # Debug print

    return render_template("index.html", year=year, month=month, holidays=holidays, calendar=month_days, lunar_dates=lunar_dates, today=today.day)

if __name__ == "__main__":
    app.run(debug=True)