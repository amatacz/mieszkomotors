from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, \
    DeleteView, UpdateView

from mieszkomotors.models.events import CarEvent, InsuranceEvent, GenericEvent
from mieszkomotors.forms import GenericEventForm


# All events list view
class EventList(LoginRequiredMixin, ListView):
    model = GenericEvent
    template_name = 'mieszkomotors/events/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generic_events'] = GenericEvent.objects.all()
        context['car_events'] = CarEvent.objects.all()
        context['insurance_events'] = InsuranceEvent.objects.all()
        return context


# Generic Events Views
class GenericEventCreateView(LoginRequiredMixin, CreateView):
    model = GenericEvent
    form_class = GenericEventForm
    template_name = 'mieszkomotors/events/generic/create.html'
    success_url = reverse_lazy('home')


class GenericEventDetailView(LoginRequiredMixin, DetailView):
    model = GenericEvent
    template_name = "mieszkomotors/events/generic/detail.html"


class GenericEventUpdateView(LoginRequiredMixin, UpdateView):
    model = GenericEvent
    template_name = "mieszkomotors/events/generic/update.html"
    form_class = GenericEventForm
    success_url = reverse_lazy('events_list')


class GenericEventDeleteView(LoginRequiredMixin, DeleteView):
    model = GenericEvent
    template_name = 'mieszkomotors/events/generic/delete.html'
    success_url = reverse_lazy('events_list')


# Car Event View
class CarEventDetailView(LoginRequiredMixin, DetailView):
    model = CarEvent
    template_name = "mieszkomotors/events/car_event_detail.html"


# Insurance Event View
class InsuranceEventDetailView(LoginRequiredMixin, DetailView):
    model = InsuranceEvent
    template_name = "mieszkomotors/events/insurance_event_detail.html"
