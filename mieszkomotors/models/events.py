from django.db import models

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
    
# na kazdt ev, mail obj + pole json (zaciaga słownik z criba), send mail

# Email sending function
    def send_email(self, *args, **options):  
        today = str(datetime.date.today().strftime('%Y-%m-%d'))

# to rusza celery, zmienia status na done/error (try)

        # Sending emails for car related events
        with open("mieszkomotors/data/car_events_data.json", 'r') as file:
            car_events = json.load(file)
  
        for car_event in car_events:
            subject = f"Zbliża się termin przeglądu dla auta {car_event[today]['license_plates']}"

            html_body = render_to_string("../templates/emails/car_email.html", car_event[today])

            email_from = settings.EMAIL_HOST_USER
            #recipient_list = settings.EMAIL_HOST_USER
            recipient_list = car_event[today]['email']
            print(recipient_list)
            message = EmailMultiAlternatives(subject, "text_body", email_from, [recipient_list])
            message.attach_alternative(html_body, "text/html")
            message.send()
        
        # Sending emails for insurance related events
    # Email sending function
    def send_email(self, *args, **options):  
        today = str(datetime.date.today().strftime('%Y-%m-%d'))
    
        with open('mieszkomotors/data/insurance_events_data.json', 'r') as file:
            insurance_events = json.load(file)

        for insurance_event in insurance_events:
            subject = f"Zbliża się termin odnowienia ubezpieczenia dla auta {insurance_event[today]['car']}."

            html_body = render_to_string("../templates/emails/insurance_email.html", insurance_event[today])

            email_from = settings.EMAIL_HOST_USER
            #recipient_list = settings.EMAIL_HOST_USER
            recipient_list = insurance_event[today]['email']
            print(recipient_list)
            message = EmailMultiAlternatives(subject, "text_body", email_from, [recipient_list])
            message.attach_alternative(html_body, "text/html")
            message.send()



        
            