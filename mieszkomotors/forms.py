from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models
from django.forms import ModelForm, TextInput, EmailInput, FileInput, NumberInput, DateInput, Select
from django.conf import settings
from django.core.mail import send_mail


class OwnerForm(ModelForm):
    class Meta:
        model = models.Owner
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        widgets = {
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
        }


class InsuranceForm(ModelForm):
    class Meta:
        model = models.Insurance
        fields = ['car', 'price', 'offer', 'current_insurance_date', 'notes', 'attachements']
        widgets = {
            "car": Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Car"
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
                "placeholder": "Current insurance date"
            }),
            "notes": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Notes"
            }),
            "attachements": FileInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Attachements"
            }),
        }



class CarForm(ModelForm):
    class Meta:
        model = models.Car
        fields = ['owner', 'brand', 'model', 'vin', 'license_plates', 'insurance', 'current_car_review_date', 'car_review_renewal_date' ,'purchase_date', 'notes', 'attachements']
        widgets = {
            "owner": Select(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Owner"
            }),
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
                "placeholder": "Next Car Review Date"
            }),
            "purchase_date": DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Purchase Date"
            }),
            "notes": TextInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Notes"
            }),
            "attachements": FileInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Attachements"
            }),


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
        model = models.User
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
        model = models.User
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

