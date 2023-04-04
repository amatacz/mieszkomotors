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

from mieszkomotors.models.car import Car, CarAttachment, CarNote
from mieszkomotors.forms import *



# Car Views 
class CarCreate(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
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
    form_class = CarForm
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
    model = CarAttachment
    form_class = CarAttachmentForm
    template_name = 'mieszkomotors/car/attachements/create.html'
    success_url = reverse_lazy('car_list')
    success_message = 'Załącznik dodany do samochodu'

    def get_initial(self):
        return {"created_by": self.request.user}

class CarAttachementsDetail(LoginRequiredMixin, DetailView):
    model = CarAttachment
    template_name = 'mieszkomotors/car/attachements/detail.html'

class CarAttachementsUpdate(LoginRequiredMixin, UpdateView):
    model = CarAttachment
    template_name = 'mieszkomotors/car/attachements/update.html'
    form_class = CarAttachmentForm
    success_url = reverse_lazy('car_list')

class CarAttachementsList(LoginRequiredMixin, ListView):
    model = CarAttachment
    template_name = 'mieszkomotors/car/attachements/list.html'

class CarAttachementsDelete(LoginRequiredMixin, DeleteView):
    model = CarAttachment
    template_name = 'mieszkomotors/car/attachements/delete.html'
    success_url = reverse_lazy('car_list')

# Car Notes Views
class CarNoteCreate(LoginRequiredMixin, CreateView):
    model = CarAttachment
    form_class = CarNoteForm
    template_name = 'mieszkomotors/car/notes/create.html'
    success_url = reverse_lazy('car_list')
    success_message = 'Notatka dodana do samochodu'

    def get_initial(self):
        return {"created_by": self.request.user}

class CarNoteDetail(LoginRequiredMixin, DetailView):
    model = CarNote
    template_name = 'mieszkomotors/car/notes/detail.html'

class CarAttachementsUpdate(LoginRequiredMixin, UpdateView):
    model = CarNote
    template_name = 'mieszkomotors/car/notes/update.html'
    form_class = CarNoteForm
    success_url = reverse_lazy('car_list')

class CarAttachementsList(LoginRequiredMixin, ListView):
    model = CarNote
    template_name = 'mieszkomotors/car/notes/list.html'

class CarNoteDelete(LoginRequiredMixin, DeleteView):
    model = CarNote
    template_name = 'mieszkomotors/car/notes/delete.html'
    success_url = reverse_lazy('car_list')

# Car Owner Views
class CarOwnerCreate(LoginRequiredMixin, CreateView):
    model = CarOwner
    form_class = CarOwnerForm
    template_name = 'mieszkomotors/car/owner/create.html'
    success_url = reverse_lazy('car_list')
    success_message = 'Właściciel dodany do bazy'

    def get_initial(self):
        return {"created_by": self.request.user}

class CarOwnerDetail(LoginRequiredMixin, DetailView):
    model = CarOwner
    template_name = 'mieszkomotors/car/owner/detail.html'

class CarOwnerUpdate(LoginRequiredMixin, UpdateView):
    model = CarOwner
    template_name = 'mieszkomotors/car/owner/update.html'
    form_class = CarOwnerForm
    success_url = reverse_lazy('car_list')

class CarOwnersList(LoginRequiredMixin, ListView):
    model = CarOwner
    template_name = 'mieszkomotors/car/owner/list.html'

class CarOwnerDelete(LoginRequiredMixin, DeleteView):
    model = CarOwner
    template_name = 'mieszkomotors/car/owner/delete.html'
    success_url = reverse_lazy('car_list')


