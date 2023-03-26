from datetime import datetime, date, timedelta
import calendar 

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

from mieszkomotors.models.car import Car, CarAttachements, CarNotes, CarIndividualOwner, CarEnterpriseOwner, CarSelfEmploedOwner



# Car Views 
class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    #form_class = CarForm
    template_name = 'mieszkomotors/car/create.html'
    success_url = reverse_lazy('car_list')
    success_message = 'Samochód dodany do bazy'

    def get_initial(self):
        return {"created_by": self.request.user}

class CarDetail(LoginRequiredMixin, DetailView):
    model = Car
    template_name = 'mieszkomotors/car/detail.html'

class CarUpdate(LoginRequiredMixin, UpdateView):
    model = Car
    template_name = 'mieszkomotors/car/update.html'
    #form_class = forms.CarForm
    success_url = reverse_lazy('car_list')

class CarList(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'mieszkomotors/car/list.html'

class CarDelete(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'mieszkomotors/car/delete.html'
    success_url = reverse_lazy('car_list')

# Car Attachements Views
class CarAttachementsCreate(LoginRequiredMixin, CreateView):
    model = CarAttachements
    #form_class = forms.CarForm
    template_name = 'mieszkomotors/car/attachements/create.html'
    success_url = reverse_lazy('car_list')
    success_message = 'Samochód dodany do bazy'

    def get_initial(self):
        return {"created_by": self.request.user}

class CarAttachementsDetail(LoginRequiredMixin, DetailView):
    model = CarAttachements
    template_name = 'mieszkomotors/car/attachements/detail.html'

class CarAttachementsUpdate(LoginRequiredMixin, UpdateView):
    model = CarAttachements
    template_name = 'mieszkomotors/car/attachements/update.html'
    #form_class = forms.CarForm
    success_url = reverse_lazy('car_list')

class CarAttachementsList(LoginRequiredMixin, ListView):
    model = CarAttachements
    template_name = 'mieszkomotors/car/attachements/list.html'

class CarAttachementsDelete(LoginRequiredMixin, DeleteView):
    model = CarAttachements
    template_name = 'mieszkomotors/car/attachements/delete.html'
    success_url = reverse_lazy('car_list')

# Car Notes Views

# Car EnterpriseOwner Views

# Car SelfEmployed Owner Views

# Car Owner Views
