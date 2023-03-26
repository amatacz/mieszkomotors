import datetime
from dateutil.relativedelta import relativedelta
from django.core.management.base import BaseCommand

from mieszkomotors import models
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        today = datetime.date.today()
        next_month = today + models.RENEWAL_INTERVAL
        cars = models.Car.objects.all().filter(car_review_renewal_date=next_month)
        insurances = models.Insurance.objects.all().filter(insurance_renewal_date = next_month)

        print(cars)
        print(insurances)

        car_events_data = []
        insurance_events_data = []

        if cars:
            for car in cars:
                car_events_data.append({str(today): {
                        'owner_first_name': car.owner.first_name,
                        'owner_last_name': car.owner.last_name,
                        'email': car.owner.email,
                        'phone': car.owner.phone_number,
                        'brand': car.brand,
                        'model': car.model,
                        'license_plates': car.license_plates,
                        'current_car_review_date' : str(car.current_car_review_date),
                        'car_review_renewal_date': str(car.car_review_renewal_date)
                    }})
            with open("mieszkomotors/data/car_events_data.json", 'w') as file:
                json.dump(car_events_data, file)

        if insurances:
            for insurance in insurances:
                insurance_events_data.append({str(today): {
                    'car': str(insurance.car),
                    'owner_first_name': insurance.car.owner.first_name,
                    'owner_last_name': insurance.car.owner.last_name,
                    'email': insurance.car.owner.email,
                    'phone': insurance.car.owner.phone_number,
                    'price': str(insurance.price),
                    'current_insurance_date': str(insurance.current_insurance_date),
                    'insurance_renewal_date': str(insurance.insurance_renewal_date),
                }})
            with open("mieszkomotors/data/insurance_events_data.json", "w") as file:
                json.dump(insurance_events_data, file)
                



