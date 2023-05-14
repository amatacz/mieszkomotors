from django.core.mail import EmailMultiAlternatives, get_connection
from django.db import models
from django.template.loader import render_to_string

from core import settings
from mieszkomotors.models.base import PublicationTracker, RENEWAL_INTERVAL
from mieszkomotors.models.car import *
from mieszkomotors.models.insurance import *



class CarEvent(PublicationTracker):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default="Default description")
    start = models.DateField(blank=True)
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.car}: {self.start.strftime("%Y-%m-%d")}'

class InsuranceEvent(PublicationTracker):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default="Default description")
    start = models.DateField(blank=True)
    end = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.insurance.car}: {self.start.strftime("%Y-%m-%d")}'
    
class WinterTyresReplacementEvent(PublicationTracker):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='winter_tyres_replacement')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start = models.DateField(default='2023-11-15')

    def __str__(self) -> str:
        return f'{self.car.license_plates} - Sezon zima {self.start.year} - {self.title}'

class SpringTyresReplacementEvent(PublicationTracker):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='spring_tyres_replacement')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start = models.DateField(default='2023-03-15')

    def __str__(self) -> str:
        return f'{self.car.license_plates} - Sezon wiosna {self.start.year} - {self.title}'

class GenericEvent(PublicationTracker):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default="Default description")
    start = models.DateField(blank=True)
    end = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.title} {self.start.strftime("%Y-%m-%d")}'
    
class CarEventMail(PublicationTracker):
    STATUSES = (
        ('p', 'pending'),
        ('s', 'sent'),
        ('r', 'running'),
        ('e', 'error')
    )
    car_event = models.ForeignKey(CarEvent, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices = STATUSES, default='p')
    email_data = models.JSONField()
    error_message = models.TextField(default='')
    created = models.DateField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f'Wiadomość dot. {self.car_event}'
    
    def send_email(self):
        self.status = 'r'
        self.save()

        subject = f"Zbliża się termin przeglądu dla auta {self.email_data['license_plates']}"
        html_body = render_to_string("../templates/emails/car_email.html", self.email_data)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = settings.EMAIL_HOST_USER
        #recipient_list = self.email_data['email']

        try:
            message = EmailMultiAlternatives(subject, "text_body", email_from, [recipient_list])
            message.attach_alternative(html_body, "text/html")
            message.send()
        except Exception as e:
            self.status = 'e'
            self.error_message = str(repr(e))
        else:
            self.status = 's'
            self.save()
        
class InsuranceEventMail(PublicationTracker):
    STATUSES = (
        ('p', 'pending'),
        ('s', 'sent'),
        ('r', 'running'),
        ('e', 'error')
    )
    status = models.CharField(max_length=1, choices = STATUSES, default='p')
    insurance_event = models.ForeignKey(InsuranceEvent, on_delete=models.CASCADE)
    email_data = models.JSONField()
    created = models.DateField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f'Wiadomość dot. {self.insurance_event}'
    

    def send_email(self):
        self.status = 'r'
        self.save()

        subject = f"Zbliża się termin odnowienia ubezpieczenia dla auta {self.email_data['car']}"
        html_body = render_to_string("../templates/emails/insurance_email.html", self.email_data)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = settings.EMAIL_HOST_USER
        #recipient_list = self.email_data['email']
        try:
            message = EmailMultiAlternatives(subject, "text_body", email_from, [recipient_list])
            message.attach_alternative(html_body, "text/html")
            message.send()
        except Exception as e:
            self.status = 'e'
            self.error_message = str(repr(e))
        else:
            self.status = 's'
            self.save()
    

class GenericEventMail(PublicationTracker):
    STATUSES = (
        ('p', 'pending'),
        ('r', 'running'),
        ('s', 'sent'),
        ('e', 'error')
    )
    generic_event = models.ForeignKey(GenericEvent, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices = STATUSES, default='p') 
    email_data = models.JSONField()
    created = models.DateField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f'Wiadomość dot. {self.generic_event}'

    def send_email(self):
        self.status = 'r'
        self.save()

        subject = f"Przypomnienie: {self}"
        html_body = render_to_string("../templates/emails/generic_email.html", self.email_data)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = settings.EMAIL_HOST_USER

        try:
            message = EmailMultiAlternatives(subject, "text_body", email_from, [recipient_list])
            message.attach_alternative(html_body, "text/html")
            message.send()
        except Exception as e:
            self.status = 'e'
            self.error_message = str(repr(e))
        else:
            self.status = 's'
            self.save()


class SpringTyresReplacementEventMail(PublicationTracker):
    STATUSES = (
        ('p', 'pending'),
        ('s', 'sent'),
        ('r', 'running'),
        ('e', 'error')
    )
    spring_tyres_replacement_event = models.ForeignKey(SpringTyresReplacementEvent, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices = STATUSES, default='p')
    email_data = models.JSONField()
    error_message = models.TextField(default='')
    created = models.DateField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f'Wiadomość dot. {self.spring_tyres_replacement_event}'
    
    def send_email(self):
        self.status = 'r'
        self.save()

        subject = f"Wymień opony na wiosenne."
        html_body = render_to_string("../templates/emails/spring_tyres_replacement_email.html", self.email_data)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = settings.EMAIL_HOST_USER
        #recipient_list = self.email_data['email']

        try:
            message = EmailMultiAlternatives(subject, "text_body", email_from, [recipient_list])
            message.attach_alternative(html_body, "text/html")
            message.send()
        except Exception as e:
            self.status = 'e'
            self.error_message = str(repr(e))
        else:
            self.status = 's'
            self.save()


class WinterTyresReplacementEventMail(PublicationTracker):
    STATUSES = (
        ('p', 'pending'),
        ('s', 'sent'),
        ('r', 'running'),
        ('e', 'error')
    )
    winter_tyres_replacement_event = models.ForeignKey(WinterTyresReplacementEvent, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices = STATUSES, default='p')
    email_data = models.JSONField()
    error_message = models.TextField(default='')
    created = models.DateField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return f'Wiadomość dot. {self.winter_tyres_replacement_event}'
    
    def send_email(self):
        self.status = 'r'
        self.save()

        subject = f"Wymień opony na zimowe."
        html_body = render_to_string("../templates/emails/winter_tyres_replacement_email.html", self.email_data)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = settings.EMAIL_HOST_USER
        #recipient_list = self.email_data['email']

        try:
            message = EmailMultiAlternatives(subject, "text_body", email_from, [recipient_list])
            message.attach_alternative(html_body, "text/html")
            message.send()
        except Exception as e:
            self.status = 'e'
            self.error_message = str(repr(e))
        else:
            self.status = 's'
            self.save()