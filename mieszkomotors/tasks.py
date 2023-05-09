from time import sleep
from celery import shared_task
from core import celery_app

from mieszkomotors.models.events import GenericEventMail, CarEventMail, InsuranceEventMail


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