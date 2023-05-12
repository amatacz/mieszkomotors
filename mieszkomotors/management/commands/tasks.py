from django.conf import settings
from django.core.management.base import BaseCommand

from mieszkomotors.tasks import handle_car_task, handle_insurance_task, handle_generic_task
from mieszkomotors.models.events import CarEventMail, InsuranceEventMail, GenericEventMail

from datetime import date

class Command(BaseCommand):
    def handle(self, *args, **options):
        today = date.today()
        pending_car_events_mails = CarEventMail.objects.filter(created = today).filter(status = 'p')
        pending_insurance_events_mails = InsuranceEventMail.objects.filter(created = today).filter(status = 'p')
        pending_generic_events_mails = GenericEventMail.objects.filter(created = today).filter(status = 'p')

        for car_email in pending_car_events_mails:
            handle_car_task.delay(car_email.id)

        for insurance_email in pending_insurance_events_mails:
            handle_insurance_task.delay(insurance_email.id)

        for generic_email in pending_generic_events_mails:
            handle_generic_task.delay(generic_email.id)


        
             