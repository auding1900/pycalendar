import holidays

class HolidayManager:
    def __init__(self, countries=None):
        if countries is None:
            countries = ['US']
        self.countries = countries
        self.holidays = self.load_holidays()

    def load_holidays(self):
        all_holidays = {}
        for country in self.countries:
            try:
                #country_holidays = holidays.CountryHoliday(country)
                country_holidays = holidays.country_holidays(country)
                # print(f"Country is {country}, Holidays: {list(country_holidays.items())}")  # Debug print
                for date, name in country_holidays.items():
                    if date not in all_holidays:
                        all_holidays[date] = name
                    else:
                        all_holidays[date] += f", {name}"
            except Exception as e:
                print(f"Error loading holidays for country {country}: {e}")
        return all_holidays

    def get_holidays(self, year, month):
        #return [(date, name) for date, name in self.holidays.items() if date.year == year and date.month == month]
        all_holidays = []
        for country in self.countries:
            x = holidays.country_holidays(country, years=year)
            for date, name in x.items():
                all_holidays.append((date, name))
        return [(date, name) for date, name in all_holidays if date.month == month]

    def set_countries(self, countries):
        self.countries = countries
        self.holidays = self.load_holidays()