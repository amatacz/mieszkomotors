from django import forms
from . import models
from django.forms import ModelForm, TextInput, EmailInput, FileInput, NumberInput, DateInput, Select

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
        fields = ['car', 'price', 'offer', 'date', 'notes', 'attachements']
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
            "date": DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Date"
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
        fields = ['owner', 'model', 'brand', 'vin', 'license_plates', 'insurance', 'car_review_date', 'purchase_date', 'notes', 'attachements']
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
            "car_review_date": DateInput(attrs={
                "class": "form-control",
                "style": "max-width: 300px",
                "placeholder": "Car Review Date"
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