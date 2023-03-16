from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=120, unique=True)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=128, null=True, blank=True)
    nip_number = models.CharField(max_length=10, null=True, blank=True)
    birthday = models.DateField(null=True)
    notes = models.TextField(max_length=500, null=True, blank=True)
    in_mieszkomotors_since = models.DateField(auto_created=True, auto_now=True)

    def __str__(self):
	    return f'{self.first_name} {self.last_name}'
    
    
class Insurance(models.Model):
    car = models.OneToOneField('Car', on_delete=models.CASCADE, related_name='car', default=666)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    offer = models.TextField(max_length=500, null=True, blank=True)
    current_insurance_date = models.DateField()
    insurance_renewal_date = models.DateField(null=True, blank=True)
    payment_1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_3 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_4 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(max_length=500, null=True, blank=True)
    attachements = models.FileField(upload_to='documents', max_length=200, blank=True)
    # insurance renewal date which will be trigger for email notifcation ?

    def __str__(self) -> str:
         return f'Insurance {self.car}'
	
	
class Car(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True, related_name='car_owner')
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    vin = models.CharField(max_length=17, unique=True)
    license_plates = models.CharField(max_length=8, unique=True)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE, related_name='car_insurance', null=True, blank=True)
    current_car_review_date = models.DateField()
    car_review_renewal_date = models.DateField(null=True, blank=True)
    purchase_date = models.DateField()
    notes = models.TextField(max_length=500, null=True, blank=True)
    in_mieszkomotors_since = models.DateField(auto_created=True, auto_now=True)
    attachements = models.FileField(upload_to='documents', max_length=200, blank=True)
    # car review renewal date which will be trigger for email notifcation ?

    def __str__(self) -> str:
         return f'{self.brand} {self.model}, owner {self.owner}'
    

class CarEvent(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    next_review_date = models.DateField(blank=True)

    @property
    def get_next_review_date(self):
        return self.car.current_car_review_date + relativedelta(months=+11)
    
    def save(self, *args, **kwargs):
         self.next_review_date = self.get_next_review_date
         super(CarEvent, self).save(*args, **kwargs)

    def __str__(self):
        return f'Owner {self.car.owner} next car review notification: {self.next_review_date}'

class InsuranceEvent(models.Model):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    next_insurance_date = models.DateField(blank=True)

    @property
    def get_next_insurance_date(self):
        return self.insurance.current_insurance_date + relativedelta(months=+11)
    
    def save(self, *args, **kwargs):
        self.next_insurance_date = self.get_next_insurance_date
        super(InsuranceEvent, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.insurance} next insurance period notification: {self.next_insurance_date}'
	
