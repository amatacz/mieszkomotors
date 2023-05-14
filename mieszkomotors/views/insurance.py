from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView

from mieszkomotors.models.insurance import Insurance, InsuranceAttachment, InsuranceNote
from mieszkomotors.forms import *


# Insurance Views
class InsuranceCreate(LoginRequiredMixin, CreateView):
    model = Insurance
    template_name = 'mieszkomotors/insurance/create.html'
    form_class = InsuranceForm
    success_url = reverse_lazy('insurance_list')
    success_message = 'Ubezpieczenie dodane do bazy'

class InsuranceDetail(LoginRequiredMixin, DetailView):
    model = Insurance
    template_name = 'mieszkomotors/insurance/detail.html'

class InsuranceUpdate(LoginRequiredMixin, UpdateView):
    model = Insurance
    template_name = 'mieszkomotors/insurance/update.html'
    form_class = InsuranceForm
    success_url = reverse_lazy('insurance_list')

class InsuranceList(LoginRequiredMixin, ListView):
    model = Insurance
    template_name = 'mieszkomotors/insurance/list.html'

class InsuranceDelete(LoginRequiredMixin, DeleteView):
    model = Insurance
    template_name = 'mieszkomotors/insurance/delete.html'
    success_url = reverse_lazy('insurance_list')


# Insurance Attachments Views
class InsuranceAttachmentCreate(LoginRequiredMixin, CreateView):
    model = InsuranceAttachment
    template_name = 'mieszkomotors/insurance/attachments/create.html'
    form_class = InsuranceAttachmentForm
    success_url = reverse_lazy('insurance_list')
    success_message = 'Ubezpieczenie dodane do bazy'

class InsuranceAttachmentDetail(LoginRequiredMixin, DetailView):
    model = InsuranceAttachment
    template_name = 'mieszkomotors/insurance/attachments/detail.html'

class InsuranceAttachmentUpdate(LoginRequiredMixin, UpdateView):
    model = InsuranceAttachment
    template_name = 'mieszkomotors/insurance/attachments/update.html'
    form_class = InsuranceAttachmentForm
    success_url = reverse_lazy('insurance_list')

class InsuranceAttachmentList(LoginRequiredMixin, ListView):
    model = InsuranceAttachment
    template_name = 'mieszkomotors/insurance/attachments/list.html'

class InsuranceAttachmentDelete(LoginRequiredMixin, DeleteView):
    model = InsuranceAttachment
    template_name = 'mieszkomotors/insurance/attachments/delete.html'
    success_url = reverse_lazy('insurance_list')


# Insurance Notes Views
class InsuranceNoteCreate(LoginRequiredMixin, CreateView):
    model = InsuranceNote
    template_name = 'mieszkomotors/insurance/notes/create.html'
    form_class = InsuranceNoteForm
    success_url = reverse_lazy('insurance_list')
    success_message = 'Ubezpieczenie dodane do bazy'

class InsuranceNoteDetail(LoginRequiredMixin, DetailView):
    model = InsuranceNote
    template_name = 'mieszkomotors/insurance/notes/detail.html'

class InsuranceNoteUpdate(LoginRequiredMixin, UpdateView):
    model = InsuranceNote
    template_name = 'mieszkomotors/insurance/notes/update.html'
    form_class = InsuranceAttachmentForm
    success_url = reverse_lazy('insurance_list')

class InsuranceNoteList(LoginRequiredMixin, ListView):
    model = InsuranceAttachment
    template_name = 'mieszkomotors/insurance/notes/list.html'

class InsuranceNoteDelete(LoginRequiredMixin, DeleteView):
    model = InsuranceNote
    template_name = 'mieszkomotors/insurance/notes/delete.html'
    success_url = reverse_lazy('insurance_list')