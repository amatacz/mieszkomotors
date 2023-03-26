from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm, TextInput, EmailInput, FileInput, NumberInput, DateInput, Select

from mieszkomotors.models.owner import IndividualOwner, IndividualOwnerAttachment, IndividualOwnerNotes
from mieszkomotors.models.owner import SelfEmployedOwner, SelfEmployedOwnerAttachment, SelfEmployedOwnerNotes
from mieszkomotors.models.car import Car

# Individual Owner Forms
class IndividualOwnerForm(ModelForm):
    class Meta:
        model = IndividualOwner
        fields = ['created_by','first_name', 'last_name', 'email', 'phone_number', 'address_prefix', 'street', 'building', 'apartment', 'city', 'zip_code', 'pesel', 'client_since']
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
            'pesel': NumberInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Pesel"
            }),
            'client_since' : DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Client since"
            }),
        }

class IndividualOwnerAttachmentForm(ModelForm):
    class Meta:
        model = IndividualOwnerAttachment
        fields = ['created_by', 'owner', 'attachment']
        widgets = {
            "created_by": forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Created By"
            }),
            'owner': forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Owner"
                }),
            'attachment': FileInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Attachment"
            })
        }
class IndividualOwnerNotesForm(ModelForm):
    class Meta:
        model = IndividualOwnerNotes
        fields = ['created_by','owner', 'note']
        widgets = {
            "created_by": forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Created By"
            }),
            'owner': forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Owner"
                }),
            'note': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Note"
            })
        }

# Self Employed Owner Forms

class SelfEmployedOwnerForm(ModelForm):
    class Meta:
        model = SelfEmployedOwner
        fields = ['created_by', 'company_name','first_name', 'last_name', 'email', 'phone_number', 
                  'address_prefix', 'street', 'building', 'apartment', 'city', 'zip_code', 'nip', 'regon', 'client_since']
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
            'nip': NumberInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "NIP"
            }),
            'regon': NumberInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "REGON"
            }),
            'client_since' : DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Client since"
            }),
        }

class SelfEmployedOwnerAttachmentForm(ModelForm):
    class Meta:
        model = SelfEmployedOwnerAttachment
        fields = ['created_by', 'owner', 'attachment']
        widgets = {
            "created_by": forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Created By"
            }),
            'owner': forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Owner"
                }),
            'attachment': FileInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Attachment"
            })
        }
class SelfEmployedNotesForm(ModelForm):
    class Meta:
        model = SelfEmployedOwnerNotes
        fields = ['created_by','owner', 'note']
        widgets = {
            "created_by": forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Created By"
            }),
            'owner': forms.Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Owner"
                }),
            'note': TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Note"
            })
        }
        
# class InsuranceForm(ModelForm):
#     class Meta:
#         model = models.Insurance
#         fields = ['car', 'price', 'offer', 'current_insurance_date', 'notes', 'attachements']
#         widgets = {
#             "car": Select(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "Car"
#             }),
#             "price": NumberInput(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "Price"
#             }),
#             "offer": TextInput(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "Offer"
#             }),
#             "current_insurance_date": DateInput(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "Current insurance date"
#             }),
#             "notes": TextInput(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "Notes"
#             }),
#             "attachements": FileInput(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "Attachements"
#             }),
#         }


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
            "vin": NumberInput(attrs={
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
                "placeholder": "Current Car Review Date"
            }),
            "car_review_renewal_date": DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Next Car Review Date",
            }),
            "purchase_date": DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Purchase Date"
            }),
        }

# # SignUpForm is not used 16.03.2023

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(max_length=150, label="Username")
#     first_name = forms.CharField(max_length=150, label="First Name")
#     last_name = forms.CharField(max_length=150, label = "Last Name")
#     email = forms.EmailInput()
#     password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
#     password2 = forms.CharField(widget=forms.PasswordInput, label="Password confirm")

#     class Meta:
#         model = models.User
#         fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
#         widget = {
#             "username": TextInput(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "Username"
#             }),

#             "first_name": TextInput(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "First Name"
#             }),
#             "last_name": TextInput(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "Last Name"
#             }),
#             "email": EmailInput(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "Email address"
#             }),
#             "password1": forms.PasswordInput(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "Password"
#             }),
#             "password2": forms.PasswordInput(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "Password confirm"
#             }),
#         }

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = models.User
#         fields = ['username', 'password']
#         widget = {
#             "username": TextInput(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "Username"
#             }),
#             "password": forms.PasswordInput(attrs={
#                 "class": "form-control",
#                 "style": "max-width: 300px",
#                 "placeholder": "Password"
#             })
#         }

