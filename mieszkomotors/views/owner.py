from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, TemplateView

from mieszkomotors.models.owner import Customer, CustomerAttachment, CustomerNote, IndividualCustomer, SelfEmployedCustomer, EnterpriseCustomer
from mieszkomotors.forms import *


# All customers list view
class CustomersList(LoginRequiredMixin, TemplateView):
    model = Customer
    template_name = 'mieszkomotors/customer/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['individual_customers'] = IndividualCustomer.objects.all()
        context['self_employed_customers'] = SelfEmployedCustomer.objects.all()
        context['enterprise_customers'] = EnterpriseCustomer.objects.all()
        return context

# Individual Customer Views 
class IndividualCustomerCreate(LoginRequiredMixin, CreateView):
    model = IndividualCustomer
    template_name = 'mieszkomotors/individual_customer/create.html'
    form_class = IndividualCustomerForm
    success_url = reverse_lazy('customers_list')
    success_message = 'Właściciel dodany do bazy'

def get_initial(self):
        return {"created_by": self.request.user}

class IndividualCustomerDetail(LoginRequiredMixin, TemplateView):
    model = IndividualCustomer
    template_name = 'mieszkomotors/individual_customer/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['individual_customers'] = IndividualCustomer.objects.all().filter(id = self.kwargs['pk'])
        context['attachments'] = CustomerAttachment.objects.all().filter(customer = self.kwargs['pk'])
        context['notes'] = CustomerNote.objects.all().filter(customer__individual_customer = self.kwargs['pk'])
        return context

class IndividualCustomerUpdate(LoginRequiredMixin, UpdateView):
    model = IndividualCustomer
    template_name = 'mieszkomotors/individual_customer/update.html'
    form_class = IndividualCustomerForm

    def get_success_url(self):
        return reverse_lazy('individual_customer_detail', kwargs={'pk': self.object.customer_id})
    
class IndividualCustomerDelete(LoginRequiredMixin, DeleteView):
    model = IndividualCustomer
    template_name = 'mieszkomotors/individual_customer/delete.html'
    success_url = reverse_lazy('customers_list')


# SelfEmployeed Customer Views 
class SelfEmployedCustomerCreate(LoginRequiredMixin, CreateView):
    model = SelfEmployedCustomer
    template_name = 'mieszkomotors/self_employed_customer/create.html'
    form_class = SelfEmployedCustomerForm
    success_url = reverse_lazy('customers_list')
    success_message = 'Właściciel dodany do bazy'

    def get_initial(self):
            return {"created_by": self.request.user}

class SelfEmployedCustomerDetail(LoginRequiredMixin, TemplateView):
    model = SelfEmployedCustomer
    context_object_name = 'customer'
    template_name = 'mieszkomotors/self_employed_customer/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['self_employed_customers'] = SelfEmployedCustomer.objects.all().filter(id = self.kwargs['pk'])
        context['attachments'] = CustomerAttachment.objects.all().filter(customer__self_employed_customer = self.kwargs['pk'])
        context['notes'] = CustomerNote.objects.all().filter(customer__self_employed_customer = self.kwargs['pk'])

        self.request.session['customer_id'] = self.kwargs['pk']

        return context

class SelfEmployedCustomerUpdate(LoginRequiredMixin, UpdateView):
    model = SelfEmployedCustomer
    template_name = 'mieszkomotors/self_employed_customer/update.html'
    form_class = SelfEmployedCustomerForm
    success_url = reverse_lazy('customers_list')

class SelfEmployedCustomerDelete(LoginRequiredMixin, DeleteView):
    model = SelfEmployedCustomer
    template_name = 'mieszkomotors/self_employed_customer/delete.html'
    success_url = reverse_lazy('customers_list')

# Enterprise Customer Views 
class EnterpriseCustomerCreate(LoginRequiredMixin, CreateView):
    model = EnterpriseCustomer
    template_name = 'mieszkomotors/enterprise_customer/create.html'
    form_class = EnterpriseCustomerForm
    success_url = reverse_lazy('customers_list')
    success_message = 'Właściciel dodany do bazy'

def get_initial(self):
        return {"created_by": self.request.user}

class EnterpriseCustomerDetail(LoginRequiredMixin, TemplateView):
    model = EnterpriseCustomer
    context_object_name = 'customer'
    template_name = 'mieszkomotors/enterprise_customer/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enterprise_customers'] = EnterpriseCustomer.objects.all().filter(id = self.kwargs['pk'])
        context['attachments'] = CustomerAttachment.objects.all().filter(customer__enterprise_customer = self.kwargs['pk'])
        context['notes'] = CustomerNote.objects.all().filter(customer__enterprise_customer = self.kwargs['pk'])

        return context

class EnterpriseCustomerUpdate(LoginRequiredMixin, UpdateView):
    model = EnterpriseCustomer
    template_name = 'mieszkomotors/enterprise_customer/update.html'
    form_class = EnterpriseCustomerForm
    success_url = reverse_lazy('customers_list')

class EnterpriseCustomerDelete(LoginRequiredMixin, DeleteView):
    model = EnterpriseCustomer
    template_name = 'mieszkomotors/enterprise_customer/delete.html'
    success_url = reverse_lazy('customers_list')


# Customer Notes Views
class CustomerNoteCreate(LoginRequiredMixin, CreateView):
    model = CustomerNote
    template_name = 'mieszkomotors/customer/notes/create.html'
    form_class = CustomerNoteForm

    def get_success_url(self):
        return reverse_lazy('customers_list')

    def get_initial(self):
        return {"created_by": self.request.user}

class CustomerNoteDetail(LoginRequiredMixin, DetailView):
    model = CustomerNote
    template_name = 'mieszkomotors/customer/notes/detail.html'

class CustomerNoteUpdate(LoginRequiredMixin, UpdateView):
    model = CustomerNote
    template_name = 'mieszkomotors/customer/notes/update.html'
    form_class = CustomerNoteForm
    success_url = reverse_lazy('customers_list')

class CustomerNoteList(LoginRequiredMixin, ListView):
    model = CustomerNote
    template_name = 'mieszkomotors/customer/notes/list.html'

class CustomerNoteDelete(LoginRequiredMixin, DeleteView):
    model = CustomerNote
    template_name = 'mieszkomotors/customer/notes/delete.html'
    success_url = reverse_lazy('customers_list')


# Customer Attachments Views
class CustomerAttachmentCreate(LoginRequiredMixin, CreateView):
    model = CustomerAttachment
    template_name = 'mieszkomotors/customer/attachments/create.html'
    form_class = CustomerAttachmentForm

    def get_success_url(self):
        return reverse_lazy('enterprise_customer_detail', kwargs={'pk': self.object.customer_id})

    def get_initial(self):
        return {"created_by": self.request.user}

class CustomerAttachmentDetail(LoginRequiredMixin, DetailView):
    model = CustomerAttachment
    template_name = 'mieszkomotors/customer/attachments/detail.html'

class CustomerAttachmentUpdate(LoginRequiredMixin, UpdateView):
    model = CustomerAttachment
    template_name = 'mieszkomotors/customer/attachments/update.html'
    form_class = CustomerAttachmentForm
    success_url = reverse_lazy('enterprise_customer_detail')

class CustomerAttachmentList(LoginRequiredMixin, ListView):
    model = CustomerAttachment
    template_name = 'mieszkomotors/customer/attachments/list.html'

class CustomerAttachmentDelete(LoginRequiredMixin, DeleteView):
    model = CustomerAttachment
    template_name = 'mieszkomotors/customer/attachments/delete.html'
    success_url = reverse_lazy('enterprise_customer_detail')