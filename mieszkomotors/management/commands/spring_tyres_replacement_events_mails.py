from django.core.management.base import BaseCommand
from mieszkomotors.models.events import Car, CarOwner,SpringTyresReplacementEvent, SpringTyresReplacementEventMail
from datetime import date

# ta komenda bedzie uruchamiana w cronie 15 marca raz w roku

'''
Command to create mail objects for each Spring Tyres Replacement Event (object assigned to each car).
Method runs once for a year, March 15th and creates SpringTyresReplacementEventMail with car and car owner data.
'''

class Command(BaseCommand):
    def handle(self, *args, **options):
        current_year = date.today().year

        spring_tyres_replacement_events = SpringTyresReplacementEvent.objects.filter(start__year = current_year)

        if spring_tyres_replacement_events:
            for spring_tyres_replacement_event in spring_tyres_replacement_events:
                owner = CarOwner.objects.filter(car=spring_tyres_replacement_event.car.pk).filter(status = 'a')[0]

                if hasattr(owner.client, 'individual_customer'):
                    spring_tyres_replacement_event_data = {
                            'owner_first_name': owner.client.individual_customer.first_name,
                            'owner_last_name': owner.client.individual_customer.last_name,
                            'email': owner.client.individual_customer.email,
                            'phone': str(owner.client.individual_customer.phone_number),
                            'brand': owner.car.brand,
                            'model': owner.car.model,
                            'license_plates': owner.car.license_plates,
                        }
                    SpringTyresReplacementEventMail.objects.create(
                        spring_tyres_replacement_event = spring_tyres_replacement_event,
                        email_data = spring_tyres_replacement_event_data
                    )
                if hasattr(owner.client, 'self_employed_customer'):
                    spring_tyres_replacement_event_data = {
                            'owner_first_name': owner.client.self_employed_customer.first_name,
                            'owner_last_name': owner.client.self_employed_customer.last_name,
                            'owner_company_name': owner.client.self_employed_customer.company_name,
                            'email': owner.client.self_employed_customer.email,
                            'phone': str(owner.client.self_employed_customer.phone_number),
                            'brand': owner.car.brand,
                            'model': owner.car.model,
                            'license_plates': owner.car.license_plates,
                        }
                    SpringTyresReplacementEventMail.objects.create(
                        spring_tyres_replacement_event = spring_tyres_replacement_event,
                        email_data = spring_tyres_replacement_event_data
                    )
                if hasattr(owner.client, 'enterprise_customer'):
                    spring_tyres_replacement_event_data = {
                            'email': owner.client.enterprise_customer.email,
                            'phone': str(owner.client.enterprise_customer.phone_number),
                            'brand': owner.car.brand,
                            'model': owner.car.model,
                            'license_plates': owner.car.license_plates,
                        }
                    SpringTyresReplacementEventMail.objects.create(
                        spring_tyres_replacement_event = spring_tyres_replacement_event,
                        email_data = spring_tyres_replacement_event_data
                    )