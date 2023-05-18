from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput, FileInput, NumberInput, DateInput, Select

from mieszkomotors.models.car import Car, CarNote, CarAttachment, CarOwner
from mieszkomotors.models.events import GenericEvent
from mieszkomotors.models.insurance import Insurance, InsuranceAttachment, InsuranceNote
from mieszkomotors.models.owner import IndividualCustomer, SelfEmployedCustomer, EnterpriseCustomer, CustomerAttachment, CustomerNote


# Individual Owner Form
class IndividualCustomerForm(ModelForm):
    class Meta:
        model = IndividualCustomer
        fields = ['created_by','first_name', 'last_name', 'email', 'phone_number', 'address_prefix', 'street', 'building', 'apartment', 'city', 'zip_code', 'pesel', 'driving_license_since' ,'customer_type', 'client_since']
        widgets = {
            "created_by": forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Created By"
            }),
            "first_name": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "First Name"
            }),
            "last_name": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Last Name"
            }),
            "email": EmailInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Email"
            }),
            "phone_number": NumberInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Phone Number"
            }),
            'address_prefix': forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Address prefix"
            }),
            'street': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Street"
            }),
            'building': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Building"
            }),
            'apartment': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Apartment"
            }),
            'city' : TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "City"
            }),
            'zip_code': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Zip Code"
            }),
            'pesel': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Pesel"
            }),
            'driving_license_since': DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "(YYYY-MM-DD)"
            }),
            'customer_type': Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Customer Type"
            }),
            'client_since' : DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "(YYYY-MM-DD)"
            }),
        }

class SelfEmployedCustomerForm(ModelForm):
    class Meta:
        model = SelfEmployedCustomer
        fields = ['created_by', 'company_name','first_name', 'last_name', 'email', 'phone_number', 
                  'address_prefix', 'street', 'building', 'apartment', 'city', 'zip_code', 'pesel', 'nip', 'regon', 'driving_license_since', 'customer_type', 'client_since']
        widgets = {
            "created_by": forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Created By"
            }),            
            "company_name": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Company Name"
            }),
            "first_name": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "First Name"
            }),
            "last_name": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Last Name"
            }),
            "email": EmailInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Email"
            }),
            "phone_number": NumberInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Phone Number"
            }),
            'address_prefix': forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Address prefix"
            }),
            'street': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Street"
            }),
            'building': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Building"
            }),
            'apartment': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Apartment"
            }),
            'city' : TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "City"
            }),
            'zip_code': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Zip Code"
            }),
            'pesel': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "PESEL"
            }),
            'nip': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "NIP"
            }),
            'regon': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "REGON"
            }),
            'driving_license_since': DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "(YYYY-MM-DD)"
            }),
            'customer_type': Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Customer Type"
            }),
            'client_since' : DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "(YYYY-MM-DD)"
            }),
        }

class EnterpriseCustomerForm(ModelForm):
    class Meta:
        model = EnterpriseCustomer
        fields = ['created_by', 'company_name', 'email', 'phone_number', 
                  'address_prefix', 'street', 'building', 'apartment', 'city', 'zip_code', 'nip', 'regon', 'customer_type', 'client_since']
        widgets = {
            "created_by": forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Created By"
            }),            
            "company_name": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Company Name"
            }),
            "email": EmailInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Email"
            }),
            "phone_number": NumberInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Phone Number"
            }),
            'address_prefix': forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Address prefix"
            }),
            'street': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Street"
            }),
            'building': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Building"
            }),
            'apartment': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Apartment"
            }),
            'city' : TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "City"
            }),
            'zip_code': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Zip Code"
            }),
            'nip': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "NIP"
            }),
            'regon': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "REGON"
            }),
            'customer_type': Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Customer Type"
            }),
            'client_since' : DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "(YYYY-MM-DD)"
            }),
        }

class CustomerAttachmentForm(ModelForm):
    class Meta:
        model = CustomerAttachment
        fields = ['created_by', 'customer', 'attachment']
        widgets = {
            "created_by": forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Created By"
            }),
            'customer': forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Customer"
                }),
            'attachment': FileInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Attachment"
            })
        }

class CustomerNoteForm(ModelForm):
    class Meta:
        model = CustomerNote
        fields = ['created_by','customer', 'note']
        widgets = {
            "created_by": forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Created By"
            }),
            'customer': forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Customer"
                }),
            'note': forms.Textarea(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Note"
            })
        }

# Insurance forms

class InsuranceForm(ModelForm):
    class Meta:
        model = Insurance
        fields = ['car', 'owner', 'price', 'offer', 'current_insurance_date']
        widgets = {
            "car": Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Car"
            }),
            'owner': Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Owner"
            }),
            "price": NumberInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Price"
            }),
            "offer": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Offer"
            }),
            "current_insurance_date": DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "(YYYY-MM-DD)"
            })
        }

class InsuranceAttachmentForm(ModelForm):
    class Meta:
        model = InsuranceAttachment
        fields = ['created_by', 'insurance', 'attachment']
        widgets = {
            "created_by": forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Created By"
            }),
            'insurance': forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Insurance"
                }),
            'attachment': FileInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Attachment"
            })
        }

class InsuranceNoteForm(ModelForm):
    class Meta:
        model = InsuranceNote
        fields = ['created_by','insurance', 'note']
        widgets = {
            "created_by": forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Created By"
            }),
            'insurance': forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Insurance"
                }),
            'note': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Note"
            })
        }

# Car Forms
class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'vin', 'license_plates', 'insurance', 'current_car_review_date', 'car_review_renewal_date' ,'purchase_date']
        widgets = {
            "brand": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Brand"
            }),
            "model": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Model"
            }),
            "vin": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Vin"
            }),
            "license_plates": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "License Plates"
            }),
            "insurance": Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Insurance"
            }),
            "current_car_review_date": DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "(YYYY-MM-DD)"
            }),
            "car_review_renewal_date": DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "(YYYY-MM-DD)",
            }),
            "purchase_date": DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "(YYYY-MM-DD)"
            }),
        }

class CarOwnerForm(ModelForm):
    class Meta:
        model = CarOwner
        fields = ['client', 'car', 'status']
        widgets = {
            'client': Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Client"
            }),
            'car': Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Car"
            }),
            'status': Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Status"
            }),
        }


class CarAttachmentForm(ModelForm):
    class Meta:
        model = CarAttachment
        fields = ['created_by', 'car', 'attachment']
        widgets = {
            "created_by": forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Created By"
            }),
            'car': forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Car"
                }),
            'attachment': FileInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Attachment"
            })
        }
class CarNoteForm(ModelForm):
    class Meta:
        model = CarNote
        fields = ['created_by','car', 'note']
        widgets = {
            "created_by": forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Created By"
            }),
            'car': forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Car"
                }),
            'note': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Note"
            })
        }

# GenericEvent Form

class GenericEventForm(ModelForm):
    class Meta:
        model = GenericEvent
        fields = ['title', 'description', 'start', 'end']
        widget = {
            "title": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Title"
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Description"
            }),
            "start": DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "(YYYY-MM-DD)"
            }),
            "end": DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "(YYYY-MM-DD)"
            })
        }

# SignUpForm is not used 16.03.2023

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, label="Username")
    first_name = forms.CharField(max_length=150, label="First Name")
    last_name = forms.CharField(max_length=150, label = "Last Name")
    email = forms.EmailInput()
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Password confirm")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        widget = {
            "username": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Username"
            }),

            "first_name": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "First Name"
            }),
            "last_name": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Last Name"
            }),
            "email": EmailInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Email address"
            }),
            "password1": forms.PasswordInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Password"
            }),
            "password2": forms.PasswordInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Password confirm"
            }),
        }

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widget = {
            "username": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Username"
            }),
            "password": forms.PasswordInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Password"
            })
        }

