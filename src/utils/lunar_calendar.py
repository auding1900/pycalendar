import calendar
from lunarcalendar import Converter, Solar

class LunarCalendar:
    def get_lunar_dates(self, year, month):
        lunar_dates = []
        cal = calendar.Calendar()
        month_days = cal.monthdayscalendar(year, month)
        for week in month_days:
            lunar_week = []
            for day in week:
                if day == 0:
                    lunar_week.append("")
                else:
                    solar_date = Solar(year, month, day)
                    lunar_date = Converter.Solar2Lunar(solar_date)
                    lunar_day = lunar_date.day
                    lunar_day_name = self.get_lunar_day_name(lunar_day)
                    lunar_week.append(f"{lunar_day_name}")
            lunar_dates.append(lunar_week)
        return lunar_dates

    def get_lunar_day_name(self, day):
        lunar_day_names = [
            "初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
            "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十",
            "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"
        ]
        return lunar_day_names[day - 1]