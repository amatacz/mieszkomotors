from datetime import datetime, date, timedelta
# import calendar 

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, View
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from mieszkomotors.models.car import Car
from mieszkomotors.models.insurance import Insurance
#from mieszkomotors.utils import Calendar

# Calendar Views

class CalendarView(ListView):
    model = Car
    template_name = 'calendar.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['carevents'] = Car.objects.all()
#         context['insuranceevents'] = Insurance.objects.all()
        
#         # use today's date for the calendar
#         d = get_date(self.request.GET.get('month', None))


#         # Instantiate our calendar class with today's year and a date
#         cal = Calendar(d.year, d.month)

#         # Call the formatmonth method, wich returns our calendar as a table
#         html_cal = cal.formatmonth(withyear=True)
#         context['calendar'] = mark_safe(html_cal)
#         context['prev_month'] = prev_month(d)
#         context['next_month'] = next_month(d)
#         context['today'] = datetime.today().month

#         return context
        
# def get_date(req_day):
#     if req_day:
#         year, month = (int(x) for x in req_day.split('-'))
#         return date(year, month, day=1)
#     return datetime.today()

# def prev_month(d):
#     first = d.replace(day=1)
#     prev_month = first - timedelta(days=1)
#     month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
#     return month

# def next_month(d):
#     days_in_month = calendar.monthrange(d.year, d.month)[1]
#     last = d.replace(day=days_in_month)
#     next_month = last + timedelta(days=1)
#     month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
#     return month
