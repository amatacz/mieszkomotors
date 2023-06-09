from datetime import date
from django.core.management.base import BaseCommand
from mieszkomotors.tasks import handle_winter_tyres_task
from mieszkomotors.models.events import WinterTyresReplacementEventMail


class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Method that sends reminder email about spring tyres replacement
        to each Car Owner using Celery Shared Tasks.
        """
        current_year = date.today().year
        pending_winter_tyres_replacement_events_mails = \
            WinterTyresReplacementEventMail.objects.filter(
                created__year=current_year).filter(status='p')

        for spring_tyres_replacement_event_mail in \
                pending_winter_tyres_replacement_events_mails:
            handle_winter_tyres_task.delay(
                spring_tyres_replacement_event_mail.id)
