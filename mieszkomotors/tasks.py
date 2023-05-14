from celery import shared_task
from core import celery_app
from time import sleep

from mieszkomotors.models.events import *


@shared_task()
def handle_car_task(car_email):
    sleep(3)
    obj = CarEventMail.objects.get(id=car_email)
    print(obj)
    obj.send_email()

@shared_task()
def handle_insurance_task(insurance_email):
    sleep(3)
    obj = InsuranceEventMail.objects.get(id=insurance_email)
    print(obj)
    obj.send_email()

@shared_task()
def handle_generic_task(generic_email):
    sleep(3)
    obj = GenericEventMail.objects.get(id=generic_email)
    print(obj)
    obj.send_email()

@shared_task()
def handle_spring_tyres_task(spring_tyres_replacement_event_mail):
    sleep(3)
    obj = SpringTyresReplacementEventMail.objects.get(id=spring_tyres_replacement_event_mail)
    print(obj)
    obj.send_email()

@shared_task()
def handle_winter_tyres_task(winter_tyres_replacement_event_mail):
    sleep(3)
    obj = WinterTyresReplacementEventMail.objects.get(id=winter_tyres_replacement_event_mail)
    print(obj)
    obj.send_email()