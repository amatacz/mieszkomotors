from django.db.models.signals import post_save
from django.dispatch import receiver
from mieszkomotors.models import Insurance, Car, CarEvent, InsuranceEvent

@receiver(post_save, sender=Car)
def create_car_reviev_event(sender, instance, created, **kwargs):
    if created:
        CarEvent.objects.create(car=instance)

@receiver(post_save, sender=Insurance)
def create_insurance_event(sender, instance, created, **kwargs):
    if created:
        InsuranceEvent.objects.create(insurance=instance)

@receiver(post_save, sender=Insurance)
def assign_insurance_to_car(sender, instance, created, **kwargs):
    if created:
        updated_car = Car.objects.get(pk=instance.car.id)
        updated_car.insurance = instance
        updated_car.save(update_fields=['insurance'])