from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import ListView, TemplateView

from mieszkomotors.models.owner import Customer, CustomerAttachment, CustomerNote
from mieszkomotors.forms import *


# All owners list view
class OwnersList(LoginRequiredMixin, TemplateView):
    model = Customer
    template_name = 'mieszkomotors/owner/list.html'

# # Individual Owner Views 
# class IndividualOwnerCreate(LoginRequiredMixin, CreateView):
#     model = Customer
#     template_name = 'mieszkomotors/owner/create.html'
#     form_class = IndividualOwnerForm
#     success_url = reverse_lazy('owner_list')
#     success_message = 'Właściciel dodany do bazy'

# def get_initial(self):
#         return {"created_by": self.request.user}

# class IndividualOwnerDetail(LoginRequiredMixin, TemplateView):
#     model = IndividualOwner
#     context_object_name = 'owner'
#     template_name = 'mieszkomotors/owner/detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['individual_owners'] = Customer.objects.all().filter(id = self.kwargs['pk'])
#         context['attachments'] = CustomerAttachment.objects.all().filter(owner = self.kwargs['pk'])
#         context['notes'] = CustomerNote.objects.all().filter(owner = self.kwargs['pk'])
#         return context

# class IndividualOwnerUpdate(LoginRequiredMixin, UpdateView):
#     model = Customer
#     template_name = 'mieszkomotors/owner/update.html'
#     form_class = IndividualOwnerForm
#     success_url = reverse_lazy('owner_list')

# class IndividualOwnerDelete(LoginRequiredMixin, DeleteView):
#     model = Customer
#     template_name = 'mieszkomotors/owner/delete.html'
#     success_url = reverse_lazy('owner_list')

# # Individual Owner Attachment Views
# class IndividualOwnerAttachmentCreate(LoginRequiredMixin, CreateView):
#     model = CustomerAttachment
#     template_name = 'mieszkomotors/owner/attachments/create.html'
#     form_class = IndividualOwnerAttachmentForm

#     def get_success_url(self):
#         return reverse_lazy('owner_detail', kwargs={'pk': self.object.owner_id})

#     def get_initial(self):
#         return {"created_by": self.request.user}

# class IndividualOwnerAttachmentDetail(LoginRequiredMixin, DetailView):
#     model = CustomerAttachment
#     template_name = 'mieszkomotors/owner/attachments/detail.html'

# class IndividualOwnerAttachmentUpdate(LoginRequiredMixin, UpdateView):
#     model = IndividualOwnerAttachment
#     template_name = 'mieszkomotors/owner/attachments/update.html'
#     form_class = IndividualOwnerAttachmentForm
#     success_url = reverse_lazy('owner_detail')

# class IndividualOwnerAttachmentList(LoginRequiredMixin, ListView):
#     model = IndividualOwnerAttachment
#     template_name = 'mieszkomotors/owner/attachments/list.html'

# class IndividualOwnerAttachmentDelete(LoginRequiredMixin, DeleteView):
#     model = IndividualOwnerAttachment
#     template_name = 'mieszkomotors/owner/attachments/delete.html'
#     success_url = reverse_lazy('owner_detail')

# # Individual Owner Notes Views
# class IndividualOwnerNotesCreate(LoginRequiredMixin, CreateView):
#     model = IndividualOwnerNotes
#     template_name = 'mieszkomotors/owner/notes/create.html'
#     form_class = IndividualOwnerNotesForm

#     def get_success_url(self):
#         return reverse_lazy('owner_detail', kwargs={'pk': self.object.owner_id})

#     def get_initial(self):
#         return {"created_by": self.request.user}

# class IndividualOwnerNotesDetail(LoginRequiredMixin, DetailView):
#     model = IndividualOwnerNotes
#     template_name = 'mieszkomotors/owner/notes/detail.html'

# class IndividualOwnerNotesUpdate(LoginRequiredMixin, UpdateView):
#     model = IndividualOwnerNotes
#     template_name = 'mieszkomotors/owner/notes/update.html'
#     form_class = IndividualOwnerNotesForm
#     success_url = reverse_lazy('owner_detail')

# class IndividualOwnerNotesList(LoginRequiredMixin, ListView):
#     model = IndividualOwnerNotes
#     template_name = 'mieszkomotors/owner/notes/list.html'

# class IndividualOwnerNotesDelete(LoginRequiredMixin, DeleteView):
#     model = IndividualOwnerNotes
#     template_name = 'mieszkomotors/owner/notes/delete.html'
#     success_url = reverse_lazy('owner_detail')



# # SelfEmployeed Owner Views 
# class SelfEmployedOwnerCreate(LoginRequiredMixin, CreateView):
#     model = SelfEmployedOwner
#     template_name = 'mieszkomotors/self_employed_owner/create.html'
#     form_class = SelfEmployedOwnerForm
#     success_url = reverse_lazy('owner_list')
#     success_message = 'Właściciel dodany do bazy'

# def get_initial(self):
#         return {"created_by": self.request.user}

# class SelfEmployedOwnerDetail(LoginRequiredMixin, TemplateView):
#     model = SelfEmployedOwner
#     context_object_name = 'owner'
#     template_name = 'mieszkomotors/self_employed_owner/detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['self_employed_owners'] = SelfEmployedOwner.objects.all().filter(id = self.kwargs['pk'])
#         context['attachments'] = SelfEmployedOwnerAttachment.objects.all().filter(owner = self.kwargs['pk'])
#         context['notes'] = SelfEmployedOwnerNotes.objects.all().filter(owner = self.kwargs['pk'])
#         return context

# class SelfEmployedOwnerUpdate(LoginRequiredMixin, UpdateView):
#     model = SelfEmployedOwner
#     template_name = 'mieszkomotors/self_employed_owner/update.html'
#     form_class = SelfEmployedOwnerForm
#     success_url = reverse_lazy('owner_list')

# class SelfEmployedOwnerDelete(LoginRequiredMixin, DeleteView):
#     model = SelfEmployedOwner
#     template_name = 'mieszkomotors/self_employed_owner/delete.html'
#     success_url = reverse_lazy('owner_list')

# # SelfEmployedOwner Owner Attachment Views

# class SelfEmployedOwnerAttachmentCreate(LoginRequiredMixin, CreateView):
#     model = SelfEmployedOwnerAttachment
#     template_name = 'mieszkomotors/self_employed_owner/attachments/create.html'
#     form_class = SelfEmployedOwnerAttachmentForm

#     def get_success_url(self):
#         return reverse_lazy('self_employed_owner_detail', kwargs={'pk': self.object.owner_id})

#     def get_initial(self):
#         return {"created_by": self.request.user}

# class SelfEmployedOwnerAttachmentDetail(LoginRequiredMixin, DetailView):
#     model = SelfEmployedOwnerAttachment
#     template_name = 'mieszkomotors/self_employed_owner/attachments/detail.html'

# class SelfEmployedOwnerAttachmentUpdate(LoginRequiredMixin, UpdateView):
#     model = IndividualOwnerAttachment
#     template_name = 'mieszkomotors/self_employed_owner/attachments/update.html'
#     form_class = SelfEmployedOwnerAttachmentForm
#     success_url = reverse_lazy('self_employed_owner_detail')

# class SelfEmployedOwnerAttachmentList(LoginRequiredMixin, ListView):
#     model = SelfEmployedOwnerAttachment
#     template_name = 'mieszkomotors/self_employed_owner/attachments/list.html'

# class SelfEmployedOwnerAttachmentDelete(LoginRequiredMixin, DeleteView):
#     model = SelfEmployedOwnerAttachment
#     template_name = 'mieszkomotors/self_employed_owner/attachments/delete.html'
#     success_url = reverse_lazy('self_employed_owner_detail')

# # SelfEmployedOwner Owner Notes Views

# class SelfEmployedOwnerNotesCreate(LoginRequiredMixin, CreateView):
#     model = SelfEmployedOwnerNotes
#     template_name = 'mieszkomotors/self_employed_owner/notes/create.html'
#     form_class = SelfEmployedNotesForm

#     def get_success_url(self):
#         return reverse_lazy('self_employed_owner_detail', kwargs={'pk': self.object.owner_id})

#     def get_initial(self):
#         return {"created_by": self.request.user}

# class SelfEmployedOwnerNotesDetail(LoginRequiredMixin, DetailView):
#     model = SelfEmployedOwnerNotes
#     template_name = 'mieszkomotors/self_employed_owner/notes/detail.html'

# class SelfEmployedOwnerNotesUpdate(LoginRequiredMixin, UpdateView):
#     model = SelfEmployedOwnerNotes
#     template_name = 'mieszkomotors/self_employed_owner/notes/update.html'
#     form_class = SelfEmployedNotesForm
#     success_url = reverse_lazy('self_employed_owner_detail')

# class SelfEmployedOwnerNotesList(LoginRequiredMixin, ListView):
#     model = SelfEmployedOwnerNotes
#     template_name = 'mieszkomotors/self_employed_owner/notes/list.html'

# class SelfEmployedOwnerNotesDelete(LoginRequiredMixin, DeleteView):
#     model = SelfEmployedOwnerNotes
#     template_name = 'mieszkomotors/self_employed_owner/notes/delete.html'
#     success_url = reverse_lazy('self_employed_owner_detail')


# # Enterprise Owner Views 
# class EnterpriseOwnerCreate(LoginRequiredMixin, CreateView):
#     model = EnterpriseOwner
#     template_name = 'mieszkomotors/enterprise_owner/create.html'
#     form_class = EnterpriseOwnerForm
#     success_url = reverse_lazy('owner_list')
#     success_message = 'Właściciel dodany do bazy'

# def get_initial(self):
#         return {"created_by": self.request.user}

# class EnterpriseOwnerDetail(LoginRequiredMixin, TemplateView):
#     model = EnterpriseOwner
#     context_object_name = 'owner'
#     template_name = 'mieszkomotors/enterprise_owner/detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['enterprise_owners'] = EnterpriseOwner.objects.all().filter(id = self.kwargs['pk'])
#         context['attachments'] = EnterpriseOwnerAttachment.objects.all().filter(owner = self.kwargs['pk'])
#         context['notes'] = EnterpriseOwnerNotes.objects.all().filter(owner = self.kwargs['pk'])
#         return context

# class EnterpriseOwnerUpdate(LoginRequiredMixin, UpdateView):
#     model = EnterpriseOwner
#     template_name = 'mieszkomotors/enterprise_owner/update.html'
#     form_class = EnterpriseOwnerForm
#     success_url = reverse_lazy('owner_list')

# class EnterpriseOwnerDelete(LoginRequiredMixin, DeleteView):
#     model = EnterpriseOwner
#     template_name = 'mieszkomotors/enterprise_owner/delete.html'
#     success_url = reverse_lazy('owner_list')

# # Enterprise Owner Attachment Views
# class EnterpriseOwnerAttachmentCreate(LoginRequiredMixin, CreateView):
#     model = EnterpriseOwnerAttachment
#     template_name = 'mieszkomotors/enterprise_owner/attachments/create.html'
#     form_class = EnterpriseOwnerAttachmentForm

#     def get_success_url(self):
#         return reverse_lazy('enterprise_owner_detail', kwargs={'pk': self.object.owner_id})

#     def get_initial(self):
#         return {"created_by": self.request.user}

# class EnterpriseOwnerAttachmentDetail(LoginRequiredMixin, DetailView):
#     model = EnterpriseOwnerAttachment
#     template_name = 'mieszkomotors/enterprise_owner/attachments/detail.html'

# class EnterpriseOwnerAttachmentUpdate(LoginRequiredMixin, UpdateView):
#     model = EnterpriseOwnerAttachment
#     template_name = 'mieszkomotors/enterprise_owner/attachments/update.html'
#     form_class = EnterpriseOwnerAttachmentForm
#     success_url = reverse_lazy('enterprise_owner_detail')

# class EnterpriseOwnerAttachmentList(LoginRequiredMixin, ListView):
#     model = EnterpriseOwnerAttachment
#     template_name = 'mieszkomotors/enterprise_owner/attachments/list.html'

# class EnterpriseOwnerAttachmentDelete(LoginRequiredMixin, DeleteView):
#     model = EnterpriseOwnerAttachment
#     template_name = 'mieszkomotors/enterprise_owner/attachments/delete.html'
#     success_url = reverse_lazy('enterprise_owner_detail')

# # Individual Owner Notes Views
# class EnterpriseOwnerNotesCreate(LoginRequiredMixin, CreateView):
#     model = EnterpriseOwnerNotes
#     template_name = 'mieszkomotors/enterprise_owner/notes/create.html'
#     form_class = EnterpriseOwnerNotesForm

#     def get_success_url(self):
#         return reverse_lazy('enterprise_owner_detail', kwargs={'pk': self.object.owner_id})

#     def get_initial(self):
#         return {"created_by": self.request.user}

# class EnterpriseOwnerNotesDetail(LoginRequiredMixin, DetailView):
#     model = EnterpriseOwnerNotes
#     template_name = 'mieszkomotors/enterprise_owner/notes/detail.html'

# class EnterpriseOwnerNotesUpdate(LoginRequiredMixin, UpdateView):
#     model = EnterpriseOwnerNotes
#     template_name = 'mieszkomotors/enterprise_owner/notes/update.html'
#     form_class = EnterpriseOwnerNotesForm
#     success_url = reverse_lazy('enterprise_owner_detail')

# class EnterpriseOwnerNotesList(LoginRequiredMixin, ListView):
#     model = EnterpriseOwnerNotes
#     template_name = 'mieszkomotors/enterprise_owner/notes/list.html'

# class EnterpriseOwnerNotesDelete(LoginRequiredMixin, DeleteView):
#     model = EnterpriseOwnerNotes
#     template_name = 'mieszkomotors/enterprise_owner/notes/delete.html'
#     success_url = reverse_lazy('enterprise_owner_detail')