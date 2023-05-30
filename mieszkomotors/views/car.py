from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

from mieszkomotors.forms import CarForm, CarAttachmentForm, \
    CarNoteForm, CarOwnerForm
from mieszkomotors.models.car import Car, CarAttachment, CarNote, CarOwner


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = Car.objects.get(id=self.kwargs['pk'])
        context['car'] = car

        try:
            CarOwner.objects.filter(car=self.kwargs['pk']).filter(status='a')
            active_owner = CarOwner.objects.filter(
                car=self.kwargs['pk']).filter(
                status='a')[0]
            context['car_owner'] = active_owner
        except CarOwner.DoesNotExist:
            pass
        return context


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


class CarNoteUpdate(LoginRequiredMixin, UpdateView):
    model = CarNote
    template_name = 'mieszkomotors/car/notes/update.html'
    form_class = CarNoteForm
    success_url = reverse_lazy('car_list')


class CarNotesList(LoginRequiredMixin, ListView):
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

    def get_context_data(self, **kwargs):
        owners = CarOwner.objects.all().filter(car=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['car_owner_list'] = owners
        return context

    def get_initial(self):
        return {"created_by": self.request.user, "car": self.kwargs['pk']}


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
