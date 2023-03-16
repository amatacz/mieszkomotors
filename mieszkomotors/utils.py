from datetime import datetime, timedelta
from calendar import HTMLCalendar
from . import models


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    
    # formats a day as a td
    # filter events by day
    def formatday(self, day, car_events, insurance_events):
        car_events_per_day = car_events.filter(next_review_date__day = day)
        insuance_events_per_day = insurance_events.filter(next_insurance_date__day = day)
        d = ""
        for car_event in car_events_per_day:
            d += f"<li> Przegląd {car_event.car.owner} {car_event.car.brand} {car_event.car.model} {car_event.next_review_date}</li>"
        for insurance_event in insuance_events_per_day:
            d += f"<li> Ubezpieczenie {insurance_event.insurance.car.owner} {insurance_event.insurance.car.brand} {insurance_event.insurance.car.model} {insurance_event.next_insurance_date} </li>"

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return "<td></td>"
    

    # formats a week as a tr
    def formatweek(self, theweek, car_events, insurance_events):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, car_events, insurance_events)
        return f"<tr> {week} </tr>"
    

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        car_events = models.CarEvent.objects.filter(next_review_date__year=self.year, next_review_date__month = self.month)
        insurance_events = models.InsuranceEvent.objects.filter(next_insurance_date__year=self.year, next_insurance_date__month = self.month)


        cal = f"<table borde='0' cellpadding='0' cellspacing='0' class='calendar'>\n"
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, car_events, insurance_events)}\n"
        return cal
    
