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

from . import models
from . import forms
from .utils import Calendar


# Insurance Views

class InsuranceCreate(LoginRequiredMixin, CreateView):
    model = models.Insurance
    template_name = 'mieszkomotors/insurance/create.html'
    form_class = forms.InsuranceForm
    success_url = reverse_lazy('insurance_list')
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