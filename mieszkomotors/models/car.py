from django.db import models

from mieszkomotors.models.owner import Customer
from mieszkomotors.models.base import PublicationTracker, get_upload_path


class Car(PublicationTracker):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    vin = models.CharField(max_length=17, unique=True)
    license_plates = models.CharField(max_length=8, unique=True)
    insurance = models.ForeignKey("Insurance", on_delete=models.CASCADE, related_name='car_insurance', null=True, blank=True)
    current_car_review_date = models.DateField()
    car_review_renewal_date = models.DateField(null=True, blank=True)
    purchase_date = models.DateField()
    in_mieszkomotors_since = models.DateField(auto_created=True, auto_now=True)
    

    def __str__(self) -> str:
         return f'{self.brand} {self.model} ({self.license_plates})'

class CarAttachment(PublicationTracker):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to=get_upload_path)
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")


class CarNote(PublicationTracker):
    car = models.ForeignKey(Car, on_delete=models.CASCADE) 
    note = models.TextField(max_length=500)
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")

    
class CarOwner(PublicationTracker):
    STATUSES = (
         ("a", "Aktywny"),
         ("n", "Nieaktywny")
	)

    client = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUSES)
    assign_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.client} {self.car}'
