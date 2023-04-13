from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import render_to_string
from django.conf import settings
from django.core.management.base import BaseCommand

import json
import datetime

class Command(BaseCommand):

    # Email sending function
    def handle(self, *args, **options):  
        today = str(datetime.date.today().strftime('%Y-%m-%d'))

        # # Sending emails for car related events
        # with open("mieszkomotors/data/car_events_data.json", 'r') as file:
        #     car_events = json.load(file)
  
        # for car_event in car_events:
        #     subject = f"Zbliża się termin przeglądu dla auta {car_event[today]['license_plates']}"

        #     html_body = render_to_string("../templates/emails/car_email.html", car_event[today])

        #     email_from = settings.EMAIL_HOST_USER
        #     #recipient_list = settings.EMAIL_HOST_USER
        #     recipient_list = car_event[today]['email']
        #     print(recipient_list)
        #     message = EmailMultiAlternatives(subject, "text_body", email_from, [recipient_list])
        #     message.attach_alternative(html_body, "text/html")
        #     message.send()
        
        # # Sending emails for insurance related events
        # with open('mieszkomotors/data/insurance_events_data.json', 'r') as file:
        #     insurance_events = json.load(file)

        # for insurance_event in insurance_events:
        #     subject = f"Zbliża się termin odnowienia ubezpieczenia dla auta {insurance_event[today]['car']}."

        #     html_body = render_to_string("../templates/emails/insurance_email.html", insurance_event[today])

        #     email_from = settings.EMAIL_HOST_USER
        #     #recipient_list = settings.EMAIL_HOST_USER
        #     recipient_list = insurance_event[today]['email']
        #     print(recipient_list)
        #     message = EmailMultiAlternatives(subject, "text_body", email_from, [recipient_list])
        #     message.attach_alternative(html_body, "text/html")
        #     message.send()

        # Sending emails for generic events
        with open("mieszkomotors/data/generic_events_data.json", 'r', encoding="utf-8") as file:
            generic_events = json.load(file)
        
        for generic_event in generic_events:
            subject = f"Przypomnienie: {generic_event[today]['title']}"

            html_body = render_to_string("../templates/emails/generic_event_email.html", generic_event[today])

            email_from = settings.EMAIL_HOST_USER
            recipient_list = 'mieszkomotors@gmail.com'
            #recipient_list = settings.EMAIL_HOST_USER
            message = EmailMultiAlternatives(subject, "text_body", email_from, [recipient_list])
            message.attach_alternative(html_body, "text/html")
            message.send()

        
            