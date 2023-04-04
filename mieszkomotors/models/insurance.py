from django.db import models
from mieszkomotors.models.car import Car
from mieszkomotors.models.owner import Customer
from mieszkomotors.models.base import PublicationTracker, get_upload_path, RENEWAL_INTERVAL


class Insurance(PublicationTracker):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car')
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='owner')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    offer = models.TextField(max_length=500, null=True, blank=True)
    current_insurance_date = models.DateField()
    insurance_renewal_date = models.DateField(null=True, blank=True)
    partial_payments = models.ForeignKey("InsurancePartialPayments", on_delete=models.CASCADE, related_name="partial_payment", null=True, blank=True)

    def __str__(self) -> str:
         return f'Insurance {self.car}'

class InsurancePartialPayments(PublicationTracker):
    STATUSES = (
         ("p", "Zapłacona"),
         ("np", "Niezapłacona"),
         ("o", "Opóźniona")
    )
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    payment_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_1_status = models.CharField(max_length=2, choices=STATUSES)
    payment_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_2_status = models.CharField(max_length=2, choices=STATUSES)
    payment_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_3_status = models.CharField(max_length=2, choices=STATUSES)
    payment_4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_4_status = models.CharField(max_length=2, choices=STATUSES)

    def __str__(self) -> str:
        return f'{self.insurance} partial payments'

class InsuranceAttachement(PublicationTracker):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    attachement = models.FileField(upload_to=get_upload_path)

class InsuranceNotes(PublicationTracker):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    notes = models.TextField(max_length=500)