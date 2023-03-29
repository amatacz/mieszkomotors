from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime

from mieszkomotors.models.base import RENEWAL_INTERVAL
from mieszkomotors.models.car import Car
from mieszkomotors.models.insurance import Insurance
from mieszkomotors.models.events import CarEvent, InsuranceEvent

# Set all car review date related fields when car review date is set
@receiver(post_save, sender=Car)
def set_car_review_dates(sender, instance, created, **kwargs):
    if created:
        instance.car_review_renewal_date = instance.current_car_review_date + relativedelta(years=+1)
        instance.save()

# Updates all car review date related fields when car review date is changed

@receiver(pre_save, sender=Car)
def change_car_review_dates(sender, instance, **kwargs):
    try:
        updated_car = Car.objects.get(id=instance.id)
        if updated_car.current_car_review_date != instance.current_car_review_date:
            instance.car_review_renewal_date = instance.current_car_review_date + relativedelta(years=+1)
            updated_car.save()
    except Car.DoesNotExist:
        return None

# Set all insurance related date fields when insurance date is set
@receiver(post_save, sender=Insurance)
def set_insurance_date(sender, instance, created, **kwargs):
    if created:
        instance.insurance_renewal_date = instance.current_insurance_date + relativedelta(years=+1)
        instance.save()

# Updates all insurance date related fields when insurance date is changed
@receiver(pre_save, sender=Insurance)
def change_insurance_dates(sender, instance, **kwargs):
    try:
        updated_insurance = Insurance.objects.get(id=instance.id)
        if updated_insurance.current_insurance_date != instance.current_insurance_date:
            instance.insurance_renewal_date = instance.current_insurance_date + relativedelta(years=+1)
            updated_insurance.save()
    except Insurance.DoesNotExist:
        return None

# Assignes insurance as FK to Car object when Insurance obj is created
@receiver(post_save, sender=Insurance)
def assign_insurance_to_car(sender, instance, created, **kwargs):
    if created:
        updated_car = Car.objects.get(pk=instance.car.id)
        updated_car.insurance = instance
        updated_car.save(update_fields=['insurance'])

# Create events when Car or Insurance is created
@receiver(post_save, sender=Car)
def create_car_event(sender, instance, created, **kwargs):
    if created:
        title = f'Zbliża się termin odnowienia przeglądu technicznego dla samochodu'
        start = datetime.today()

        car_event = CarEvent.objects.create(car=instance, title=title, start=start)
        car_event.title = f'Zbliża się termin odnowienia przeglądu technicznego dla samochodu {car_event.car.license_plates}'
        car_event.start = car_event.car.car_review_renewal_date - timedelta(days=RENEWAL_INTERVAL)

        car_event.save()

@receiver(post_save, sender=Insurance)
def create_insurance_event(sender, instance, created, **kwargs):
    if created:
        title = f'Zbliża się termin odnowienia ubezpieczenia dla samochodu'
        start = datetime.today()

        insurance_event = InsuranceEvent.objects.create(insurance=instance, title=title, start=start)
        insurance_event.title = f'Zbliża się termin odnowienia ubezpieczenia dla samochodu {insurance_event.insurance.car.license_plates}'
        insurance_event.start = insurance_event.insurance.insurance_renewal_date - timedelta(days=RENEWAL_INTERVAL)

        insurance_event.save()



# do poprawy!!!!
# Update Events dates when Car or Insurance dates are updated
@receiver(pre_save, sender=Insurance)
def change_insurance_event_dates(sender, instance, **kwargs):
    try:
        updated_insurance_event = InsuranceEvent.objects.get(id=instance.id)
        if updated_insurance_event.insurance.current_insurance_date != instance.current_insurance_date:
            updated_insurance_event.start = updated_insurance_event.insurance.insurance_renewal_date - timedelta(days=RENEWAL_INTERVAL)
            updated_insurance_event.save()

    except InsuranceEvent.DoesNotExist:
        return None
    
@receiver(pre_save, sender=Car)
def change_car_event_dates(sender, instance, **kwargs):
    try:
        updated_car_event = CarEvent.objects.get(id=instance.id)
        if updated_car_event.car.current_car_review_date != instance.current_car_review_date:
            updated_car_event.start = updated_car_event.car.car_review_renewal_date - timedelta(days=RENEWAL_INTERVAL)
            updated_car_event.save()
    except CarEvent.DoesNotExist:
        return None




