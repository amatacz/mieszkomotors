import datetime
import json

from django.core.management.base import BaseCommand

from mieszkomotors.models.events import *
from mieszkomotors.models.base import RENEWAL_INTERVAL


class Command(BaseCommand):
    def handle(self, *args, **options):
        today = datetime.date.today()
        carevents = CarEvent.objects.all().filter(start=today)
        insurance_events = InsuranceEvent.objects.all().filter(start=today)

        car_events_data = []
        insurance_events_data = []

        if carevents:
            for carevent in carevents:
                owner = CarOwner.objects.all().filter(car=carevent.car.pk)[0]
                
                if hasattr(owner.client, 'individual_customer'):
                    car_events_data.append({str(today): {
                            'owner_first_name': owner.client.individual_customer.first_name,
                            'owner_last_name': owner.client.individual_customer.last_name,
                            'email': owner.client.individual_customer.email,
                            'phone': str(owner.client.individual_customer.phone_number),
                            'brand': carevent.car.brand,
                            'model': carevent.car.model,
                            'license_plates': carevent.car.license_plates,
                            'current_car_review_date' : str(carevent.car.current_car_review_date),
                            'car_review_renewal_date': str(carevent.car.car_review_renewal_date)
                        }})
                elif hasattr(owner.client, 'self_employed_customer'):
                    car_events_data.append({str(today): {
                            'owner_first_name': owner.client.self_employed_customer.first_name,
                            'owner_last_name': owner.client.self_employed_customer.last_name,
                            'company_name': owner.client.self_employed_customer.company_name,
                            'email': owner.client.self_employed_customer.email,
                            'phone': str(owner.client.self_employed_customer.phone_number),
                            'brand': carevent.car.brand,
                            'model': carevent.car.model,
                            'license_plates': carevent.car.license_plates,
                            'current_car_review_date' : str(carevent.car.current_car_review_date),
                            'car_review_renewal_date': str(carevent.car.car_review_renewal_date)
                        }})
                elif hasattr(owner.client, 'enterprise_customer'):
                    car_events_data.append({str(today): {
                            'company_name': owner.client.enterprise_customer.company_name,
                            'email': owner.client.enterprise_customer.email,
                            'phone': str(owner.client.enterprise_customer.phone_number),
                            'brand': carevent.car.brand,
                            'model': carevent.car.model,
                            'license_plates': carevent.car.license_plates,
                            'current_car_review_date' : str(carevent.car.current_car_review_date),
                            'car_review_renewal_date': str(carevent.car.car_review_renewal_date)
                        }})
                else:
                    pass
            with open("mieszkomotors/data/car_events_data.json", 'w') as file:
                json.dump(car_events_data, file)

        if insurance_events:
            for insurance_event in insurance_events:
                owner = CarOwner.objects.all().filter(car=insurance_event.insurance.car.pk)[0]
                
                if hasattr(owner.client, 'individual_customer'):
                    insurance_events_data.append({str(today): {
                        'car': str(insurance_event.insurance.car),
                        'owner_first_name': owner.client.individual_customer.first_name,
                        'owner_last_name': owner.client.individual_customer.last_name,
                        'email': owner.client.individual_customer.email,
                        'phone': str(owner.client.individual_customer.phone_number),
                        'price': str(insurance_event.insurance.price),
                        'current_insurance_date': str(insurance_event.insurance.current_insurance_date),
                        'insurance_renewal_date': str(insurance_event.insurance.insurance_renewal_date),
                    }})
                elif hasattr(owner.client, 'self_employed_customer'):
                    insurance_events_data.append({str(today): {
                        'car': str(insurance_event.insurance.car),
                        'owner_first_name': owner.client.self_employed_customer.first_name,
                        'owner_last_name': owner.client.self_employed_customer.last_name,
                        'company_name': owner.client.self_employed_customer.company_name,
                        'email': owner.client.self_employed_customer.email,
                        'phone': str(owner.client.self_employed_customer.phone_number),
                        'price': str(insurance_event.insurance.price),
                        'current_insurance_date': str(insurance_event.insurance.current_insurance_date),
                        'insurance_renewal_date': str(insurance_event.insurance.insurance_renewal_date),
                    }})
                elif hasattr(owner.client, 'enterprise_customer'):
                    insurance_events_data.append({str(today): {
                        'car': str(insurance_event.insurance.car),
                        'company_name': owner.client.enterprise_customer.company_name,
                        'email': owner.client.enterprise_customer.email,
                        'phone': str(owner.client.enterprise_customer.phone_number),
                        'price': str(insurance_event.insurance.price),
                        'current_insurance_date': str(insurance_event.insurance.current_insurance_date),
                        'insurance_renewal_date': str(insurance_event.insurance.insurance_renewal_date),
                    }})                   
            with open("mieszkomotors/data/insurance_events_data.json", "w") as file:
                json.dump(insurance_events_data, file)
                



