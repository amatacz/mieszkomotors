from datetime import date

from django.core.management.base import BaseCommand
from mieszkomotors.models.car import CarOwner
from mieszkomotors.models.events import WinterTyresReplacementEvent, \
    WinterTyresReplacementEventMail

# ta komenda bedzie uruchamiana w cronie 15 listopada raz w roku

'''
Command to create mail objects for each Winter Tyres Replacement Event
(object assigned to each car).
Method runs once for a year, November 15th and creates
WinterTyresReplacementEventMail with car and car owner data.
'''


class Command(BaseCommand):
    def handle(self, *args, **options):
        current_year = date.today().year

        winter_tyres_replacement_events = WinterTyresReplacementEvent. \
            objects.filter(start__year=current_year)

        if winter_tyres_replacement_events:
            for winter_tyres_replacement_event in \
                    winter_tyres_replacement_events:
                owner = CarOwner.objects.filter(
                    car=winter_tyres_replacement_event.car.pk).filter(
                    status='a')[0]

                if hasattr(owner.client, 'individual_customer'):
                    winter_tyres_replacement_event_data = {
                            'owner_first_name':
                            owner.client.individual_customer.first_name,
                            'owner_last_name':
                            owner.client.individual_customer.last_name,
                            'email':
                            owner.client.individual_customer.email,
                            'phone':
                            str(owner.client.individual_customer.phone_number),
                            'brand':
                            owner.car.brand,
                            'model':
                            owner.car.model,
                            'license_plates':
                            owner.car.license_plates,
                        }
                    WinterTyresReplacementEventMail.objects.create(
                        winter_tyres_replacement_event=(
                            winter_tyres_replacement_event),
                        email_data=winter_tyres_replacement_event_data
                    )
                if hasattr(owner.client, 'self_employed_customer'):
                    winter_tyres_replacement_event_data = {
                            'owner_first_name':
                            owner.client.self_employed_customer.first_name,
                            'owner_last_name':
                            owner.client.self_employed_customer.last_name,
                            'owner_company_name':
                            owner.client.self_employed_customer.company_name,
                            'email':
                            owner.client.self_employed_customer.email,
                            'phone':
                            str(owner.client.self_employed_customer.
                                phone_number),
                            'brand':
                            owner.car.brand,
                            'model':
                            owner.car.model,
                            'license_plates':
                            owner.car.license_plates,
                        }
                    WinterTyresReplacementEventMail.objects.create(
                        winter_tyres_replacement_event=(
                            winter_tyres_replacement_event),
                        email_data=winter_tyres_replacement_event_data
                    )
                if hasattr(owner.client, 'enterprise_customer'):
                    winter_tyres_replacement_event_data = {
                            'email':
                            owner.client.enterprise_customer.email,
                            'phone':
                            str(owner.client.enterprise_customer.phone_number),
                            'brand':
                            owner.car.brand,
                            'model':
                            owner.car.model,
                            'license_plates':
                            owner.car.license_plates,
                        }
                    WinterTyresReplacementEventMail.objects.create(
                        winter_tyres_replacement_event=(
                            winter_tyres_replacement_event),
                        email_data=winter_tyres_replacement_event_data
                    )
