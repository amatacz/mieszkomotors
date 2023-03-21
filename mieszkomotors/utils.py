import datetime
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

        car_events_per_day = car_events.filter(car_review_renewal_date__day = day)
        insurance_events_per_day = insurance_events.filter(insurance_renewal_date__day = day)
        d = ""
        for car_event in car_events_per_day:
            d += f"<li> Przegląd {car_event.owner} {car_event.brand} {car_event.model} {car_event.car_review_renewal_date}</li>"
        for insurance_event in insurance_events_per_day:
            d += f"<li> Ubezpieczenie {insurance_event.car.owner} {insurance_event.car.brand} {insurance_event.car.model} {insurance_event.insurance_renewal_date} </li>"

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
        car_events = models.Car.objects.filter(car_review_renewal_date__year=self.year, car_review_renewal_date__month = self.month)
        insurance_events = models.Insurance.objects.filter(insurance_renewal_date__year=self.year, insurance_renewal_date__month = self.month)


        cal = f"<table borde='0' cellpadding='0' cellspacing='0' class='calendar'>\n"
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, car_events, insurance_events)}\n"
        return cal
    
