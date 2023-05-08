from django.db import models

from core import settings
from mieszkomotors.models.base import PublicationTracker, RENEWAL_INTERVAL
from mieszkomotors.models.car import *
from mieszkomotors.models.insurance import *

from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import render_to_string
from datetime import datetime
import json

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
    
class WinterTyresReplacement(PublicationTracker):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start = models.DateField(default='2023-11-12')
    end = models.DateField(blank=True)

class SpringTyresReplacement(PublicationTracker):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start = models.DateField(default='2023-03-15')
    end = models.DateField(blank=True)

class GenericEvent(PublicationTracker):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, default="Default description")
    start = models.DateField(blank=True)
    end = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.title} {self.start.strftime("%Y-%m-%d")}'
    

# na kazdt event, mail obj + pole json (zaciaga słownik z crona), send mail
class CarEventMail(PublicationTracker):
    STATUSES = (
        ('p', 'pending'),
        ('s', 'sent'),
        ('e', 'error')
    )
    car_event = models.ForeignKey(CarEvent, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices = STATUSES, default='p')
    email_data = models.JSONField()

    def __str__(self) -> str:
        return f'Wiadomość dot. {self.car_event}'

    # # Email sending function
    # def send_email(self, *args, **options):  
    #     today = str(datetime.date.today().strftime('%Y-%m-%d'))

    # # to rusza celery, zmienia status na done/error (try)

    #     # Sending emails for car related events
    #     with open("mieszkomotors/data/car_events_data.json", 'r') as file:
    #         car_events = json.load(file)
  
    #     for car_event in car_events:
    #         subject = f"Zbliża się termin przeglądu dla auta {car_event[today]['license_plates']}"

    #         html_body = render_to_string("../templates/emails/car_email.html", car_event[today])

    #         email_from = settings.EMAIL_HOST_USER
    #         #recipient_list = settings.EMAIL_HOST_USER
    #         recipient_list = car_event[today]['email']
    #         print(recipient_list)
    #         message = EmailMultiAlternatives(subject, "text_body", email_from, [recipient_list])
    #         message.attach_alternative(html_body, "text/html")
    #         message.send()
    

class InsuranceEventMail(PublicationTracker):
    STATUSES = (
        ('p', 'pending'),
        ('s', 'sent'),
        ('e', 'error')
    )
    status = models.CharField(max_length=1, choices = STATUSES, default='p')
    insurance_event = models.ForeignKey(InsuranceEvent, on_delete=models.CASCADE)
    email_data = models.JSONField()

    def __str__(self) -> str:
        return f'Wiadomość dot. {self.insurance_event}'
    
    # # Sending emails for insurance related events
    # # Email sending function
    # def send_email(self, *args, **options):  
    #     today = str(datetime.date.today().strftime('%Y-%m-%d'))
    
    #     with open('mieszkomotors/data/insurance_events_data.json', 'r') as file:
    #         insurance_events = json.load(file)

    #     for insurance_event in insurance_events:
    #         subject = f"Zbliża się termin odnowienia ubezpieczenia dla auta {insurance_event[today]['car']}."

    #         html_body = render_to_string("../templates/emails/insurance_email.html", insurance_event[today])

    #         email_from = settings.EMAIL_HOST_USER
    #         #recipient_list = settings.EMAIL_HOST_USER
    #         recipient_list = insurance_event[today]['email']
    #         print(recipient_list)
    #         message = EmailMultiAlternatives(subject, "text_body", email_from, [recipient_list])
    #         message.attach_alternative(html_body, "text/html")
    #         message.send()


class GenericEventMail(PublicationTracker):
    STATUSES = (
        ('p', 'pending'),
        ('s', 'sent'),
        ('e', 'error')
    )
    generic_event = models.ForeignKey(GenericEvent, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices = STATUSES, default='p') 
    email_data = models.JSONField()

    def __str__(self) -> str:
        return f'Wiadomość dot. {self.generic_event}'

    # # Sending emails for generic events
    # def send_email(self, *args, **options):  
    #     today = str(datetime.date.today().strftime('%Y-%m-%d'))
    #     with open("mieszkomotors/data/generic_events_data.json", 'r', encoding="utf-8") as file:
    #         generic_events = json.load(file)
        
    #     for generic_event in generic_events:
    #         subject = f"Przypomnienie: {generic_event[today]['title']}"

    #         html_body = render_to_string("../templates/emails/generic_event_email.html", generic_event[today])

    #         email_from = settings.EMAIL_HOST_USER
    #         recipient_list = settings.EMAIL_HOST_USER
    #         message = EmailMultiAlternatives(subject, "text_body", email_from, [recipient_list])
    #         message.attach_alternative(html_body, "text/html")
    #         message.send()




        
            