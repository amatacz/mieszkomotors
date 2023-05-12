from django.core.management.base import BaseCommand

from mieszkomotors.models.events import Car, SpringTyresReplacementEvent, WinterTyresReplacementEvent

from datetime import date

'''
Method to assure that spring and winter replacement events are present for each car
or create one for object if not exist.
Methon runs once for a month in cron.
'''

class Command(BaseCommand):
    def handle(self, *args, **options):
        current_year = date.today().year

        cars = Car.objects.all()
        for car in cars:
            if not SpringTyresReplacementEvent.objects.filter(car = car).filter(start__year = current_year):
                SpringTyresReplacementEvent.objects.create(
                    car = car,
                    start = f'{current_year}-03-15',
                    title = "Zmiana opon na letnie",
                    description = "Przypominam o zmianie opon na letnie"
                )
            if not WinterTyresReplacementEvent.objects.filter(car = car).filter(start__year = current_year):
                WinterTyresReplacementEvent.objects.create(
                    car = car,
                    start = f'{current_year}-11-15',
                    title = "Zmiana opon na zimowe",
                    description = "Przypominam o zmianie opon na zimowe"                   
                )
