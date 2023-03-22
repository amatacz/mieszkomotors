from time import sleep
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
from django.core.management.base import BaseCommand
from celery import shared_task
from .management.commands import find_todays_events


@shared_task
def handle(self, *args, **options):  
    events_data = find_todays_events.handle()      
    subject = f"Zbliża się termin przeglądu dla auta {events_data['owner']}"
    print(subject)
    with get_connection(
        host = settings.EMAIL_HOST,
        port = settings.EMAIL_PORT,
        username = settings.EMAIL_HOST_USER,
        password = settings.EMAIL_HOST_PASSWORD,
        use_tls = settings.EMAIL_USE_TLS
    ) as connection:
        subject = subject
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER,]
        message = "Elo, elo 520!"
        EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
