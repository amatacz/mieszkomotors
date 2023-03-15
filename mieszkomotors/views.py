from datetime import datetime, date, timedelta
import calendar 

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.utils.safestring import mark_safe


from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from . import forms
from .utils import Calendar

# Home
def home_view(request):
    return render(request, 'home.html')

# Cars Views 
class CarCreate(LoginRequiredMixin, CreateView):
    model = models.Car
    form_class = forms.CarForm
    template_name = 'mieszkomotors/car/create.html'
    success_url = reverse_lazy('home')
    success_message = 'Samochód dodany do bazy'

class CarDetail(LoginRequiredMixin, DetailView):
    model = models.Car
    template_name = 'mieszkomotors/car/detail.html'

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = models.Car
    template_name = 'mieszkomotors/car/update.html'
    form_class = forms.CarForm
    success_url = reverse_lazy('car_list')

class CarList(LoginRequiredMixin, ListView):
    model = models.Car
    template_name = 'mieszkomotors/car/list.html'

class CarDelete(LoginRequiredMixin, DeleteView):
    model = models.Car
    template_name = 'mieszkomotors/car/delete.html'
    success_url = reverse_lazy('car_list')


# Owner Views 
class OwnerCreate(LoginRequiredMixin, CreateView):
    model = models.Owner
    template_name = 'mieszkomotors/owner/create.html'
    form_class = forms.OwnerForm
    success_url = reverse_lazy('home')
    success_message = 'Właściciel dodany do bazy'

class OwnerDetail(LoginRequiredMixin, DetailView):
    model = models.Owner
    template_name = 'mieszkomotors/owner/detail.html'

class OwnerUpdate(LoginRequiredMixin, UpdateView):
    model = models.Owner
    template_name = 'mieszkomotors/owner/update.html'
    form_class = forms.OwnerForm
    success_url = reverse_lazy('owner_list')

class OwnerList(LoginRequiredMixin, ListView):
    model = models.Owner
    template_name = 'mieszkomotors/owner/list.html'

class OwnerDelete(LoginRequiredMixin, DeleteView):
    model = models.Owner
    template_name = 'mieszkomotors/owner/delete.html'
    success_url = reverse_lazy('owner_list')

# Insurance Views
class InsuranceCreate(LoginRequiredMixin, CreateView):
    model = models.Insurance
    template_name = 'mieszkomotors/insurance/create.html'
    form_class = forms.InsuranceForm
    success_url = reverse_lazy('home')
    success_message = 'Ubezpieczenie dodane do bazy'

class InsuranceDetail(LoginRequiredMixin, DetailView):
    model = models.Insurance
    template_name = 'mieszkomotors/insurance/detail.html'

class InsuranceUpdate(LoginRequiredMixin, UpdateView):
    model = models.Insurance
    template_name = 'mieszkomotors/insurance/update.html'
    form_class = forms.InsuranceForm
    success_url = reverse_lazy('insurance_list')

class InsuranceList(LoginRequiredMixin, ListView):
    model = models.Insurance
    template_name = 'mieszkomotors/insurance/list.html'

class InsuranceDelete(LoginRequiredMixin, DeleteView):
    model = models.Insurance
    template_name = 'mieszkomotors/insurance/delete.html'
    success_url = reverse_lazy('insurance_list')

# Calendar Views

class CalendarView(LoginRequiredMixin, ListView):
    model = models.CarEvent
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carevents'] = models.Car.objects.all()
        context['insuranceevents'] = models.InsuranceEvent.objects.all()
        
        # use today's date for the calendar
        d = get_date(self.request.GET.get('month', None))


        # Instantiate our calendar class with today's year and a date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, wich returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['today'] = datetime.today().month

        return context
        
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month