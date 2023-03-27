from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django.db import models
from mieszkomotors.models.owner import IndividualOwner, EnterpriseOwner, SelfEmployedOwner
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
         return f'{self.brand} {self.model}'

class CarAttachements(PublicationTracker):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    attachements = models.FileField(upload_to=get_upload_path)

class CarNotes(PublicationTracker):
    car = models.ForeignKey(Car, on_delete=models.CASCADE) 
    notes = models.TextField(max_length=500)
    
class CarEnterpriseOwner(PublicationTracker):
    STATUSES = (
         ("a", "Aktywny"),
         ("n", "Nieaktywny")
	)
    client = models.ForeignKey(EnterpriseOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUSES)
    assign_date = models.DateTimeField(auto_now_add=True)

class CarSelfEmployedOwner(PublicationTracker):
    STATUSES = (
         ("a", "Aktywny"),
         ("n", "Nieaktywny")
	)
    client = models.ForeignKey(SelfEmployedOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUSES)
    assign_date = models.DateTimeField(auto_now_add=True)

class CarIndividualOwner(PublicationTracker):
    STATUSES = (
         ("a", "Aktywny"),
         ("n", "Nieaktywny")
	)

    # limit = models.Q(app_label = 'mieszkomotors', model = 'enterpriseowner') | models.Q(app_label = 'mieszkomotors', model = 'selfemployedowner') | models.Q(app_label = 'mieszkomotors', model = 'individualowner')
    # content_type = models.ForeignKey(ContentType, limit_choices_to=limit, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')

    client = models.ForeignKey(IndividualOwner, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUSES)
    assign_date = models.DateTimeField(auto_now_add=True)