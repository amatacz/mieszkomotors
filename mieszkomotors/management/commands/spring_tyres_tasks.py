from django.conf import settings
from django.core.management.base import BaseCommand

from mieszkomotors.tasks import handle_spring_tyres_task
from mieszkomotors.models.events import SpringTyresReplacementEventMail, CarOwner
from datetime import date

'''
Method that sends reminder email to each Car Owner using Celery Shared Tasks.
'''

class Command(BaseCommand):
    def handle(self, *args, **options):
        current_year = date.today().year
        pending_spring_tyres_replacement_events_mails = SpringTyresReplacementEventMail.objects.filter(created__year = current_year).filter(status = 'p')

        for spring_tyres_replacement_event_mail in pending_spring_tyres_replacement_events_mails:  
            handle_spring_tyres_task.delay(spring_tyres_replacement_event_mail.id)
