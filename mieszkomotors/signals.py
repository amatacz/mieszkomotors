from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from mieszkomotors.models import Insurance, Car
from dateutil.relativedelta import relativedelta
from datetime import timedelta

# Set all car review date related fields when car review date is set
@receiver(post_save, sender=Car)
def set_car_review_dates(sender, instance, created, **kwargs):
    if created:
        instance.car_review_renewal_date = instance.current_car_review_date + relativedelta(years=+1)
        instance.car_review_renewal_date_notification = instance.current_car_review_date + relativedelta(months=+11)
        instance.save()

# Updates all car review date related fields when car review date is changed
@receiver(pre_save, sender=Car)
def change_car_review_dates(sender, instance, **kwargs):
    updated_car = Car.objects.get(id=instance.id)
    if updated_car.current_car_review_date != instance.current_car_review_date:
        instance.car_review_renewal_date = instance.current_car_review_date + relativedelta(years=+1)
        instance.car_review_renewal_date_notification = instance.current_car_review_date + relativedelta(months=+11)
        updated_car.save()

# Set all insurance related date fields when insurance date is set
@receiver(post_save, sender=Insurance)
def set_insurance_date(sender, instance, created, **kwargs):
    if created:
        instance.insurance_renewal_date = instance.current_insurance_date + relativedelta(years=+1)
        instance.insurance_renewal_date_notification = instance.current_insurance_date + relativedelta(months=+11)
        instance.save()

# Updates all insurance date related fields when insurance date is changed
@receiver(pre_save, sender=Insurance)
def change_insurance_dates(sender, instance, **kwargs):
    updated_insurance = Insurance.objects.get(id=instance.id)
    if updated_insurance.current_insurance_date != instance.current_insurance_date:
        instance.insurance_renewal_date = instance.current_insurance_date + relativedelta(years=+1)
        instance.insurance_renewal_date_notification = instance.current_insurance_date + relativedelta(months=+11)
        updated_insurance.save()

# Assignes insurance as FK to Car object when Insurance obj is created
@receiver(post_save, sender=Insurance)
def assign_insurance_to_car(sender, instance, created, **kwargs):
    if created:
        updated_car = Car.objects.get(pk=instance.car.id)
        updated_car.insurance = instance
        updated_car.save(update_fields=['insurance'])