from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import render_to_string
from django.conf import settings
from django.core.management.base import BaseCommand

from mieszkomotors.models.events import CarEventMail

import json
from datetime import date, datetime

class Command(BaseCommand):
    # Email sending function
    def handle(self, *args, **options):
        today = datetime.today()
        car_events_mails = CarEventMail.objects.filter(publication_datetime = today)

        for car_event_mail in car_events_mails:
            print(car_event_mail)
            car_event_mail.send_email()
            print("Poszło!")


        
             