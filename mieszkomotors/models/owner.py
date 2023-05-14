from phonenumber_field.modelfields import PhoneNumberField

from django.db import models

from .base import PublicationTracker, get_upload_path, get_upload_path_enterprise_owner, get_file_name


class Customer(PublicationTracker):
    identifier = models.CharField(max_length=50, default="Brak identyfikatora")

    def __str__(self):
        try:
            individual_owner = IndividualCustomer.objects.get(customer = self.pk)
            return f'{individual_owner.first_name} {individual_owner.last_name}'
        except IndividualCustomer.DoesNotExist:
            try:
                self_employed_owner = SelfEmployedCustomer.objects.get(customer = self.pk)
                return f'{self_employed_owner.first_name} {self_employed_owner.last_name}'
            except SelfEmployedCustomer.DoesNotExist:
                try:
                    enterprise_owner = EnterpriseCustomer.objects.get(customer = self.pk)
                    return f'{enterprise_owner.company_name}'
                except EnterpriseCustomer.DoesNotExist:
                    return ''
                  
class CustomerAttachment(PublicationTracker):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='attachments')
    attachment = models.FileField(upload_to=get_upload_path, editable=True)
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")
    
    def __str__(self):
        return f'{self.customer}'

class CustomerNote(PublicationTracker):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='notes')
    note = models.TextField(max_length=500)
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")

    def __str__(self):
        return f'Note: {self.customer} {self.publication_datetime.date()}'
    
class ContactData(PublicationTracker):
    ADDRES_PREFIXES = (
         ("ul.", "ul."),
         ("al.", "al."),
         ("os.", "os."),
         ("pl.", "pl.")
        )

    email = models.EmailField(max_length=120, unique=True)
    phone_number = PhoneNumberField()
    address_prefix = models.CharField(max_length=3, choices=ADDRES_PREFIXES, default="ul.")
    street = models.CharField(max_length=128, null=True, blank=True)
    building = models.CharField(max_length=10)
    apartment = models.CharField(max_length=12, null=True, blank=True)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)  

    class Meta:
            abstract = True
    
class IndividualCustomer(ContactData):
    CUSTOMER_TYPE = (
          ('individual', 'IndividualCustomer'),
          ('selfemployed', 'SelfEmployedCustomer'),
          ('enterprise', 'EnterpriseCustomer')
    )
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name= 'individual_customer', null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    pesel = models.CharField(max_length=11, unique=True, verbose_name="Identyfikator - PESEL")
    driving_license_since = models.DateField(default='1970-01-01')
    customer_type = models.CharField(max_length=15, choices=CUSTOMER_TYPE, default='individual')
    client_since = models.DateField() 

    def __str__(self):
         return f'{self.first_name} {self.last_name}'

class SelfEmployedCustomer(ContactData):
    CUSTOMER_TYPE = (
          ('individual', 'IndividualCustomer'),
          ('selfemployed', 'SelfEmployedCustomer'),
          ('enterprise', 'EnterpriseCustomer')
    )

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name= 'self_employed_customer', null=True, blank=True)
    company_name = models.CharField(max_length=80)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    nip = models.CharField(max_length=10, verbose_name='NIP')
    regon = models.CharField(max_length=11, unique=True, verbose_name="Identyfikator - REGON")
    driving_license_since = models.DateField(default='1970-01-01')
    customer_type = models.CharField(max_length=15, choices=CUSTOMER_TYPE, default='selfemployed')
    client_since = models.DateField() 


    def __str__(self):
        return f'{self.company_name}'
    
class EnterpriseCustomer(ContactData):
    CUSTOMER_TYPE = (
          ('individual', 'IndividualCustomer'),
          ('selfemployed', 'SelfEmployedCustomer'),
          ('enterprise', 'EnterpriseCustomer')
    )
    
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name= 'enterprise_customer', null=True, blank=True)
    company_name = models.CharField(max_length=100)
    nip = models.CharField(max_length=10, null=True, blank=True)
    regon = models.CharField(max_length=11, unique=True, verbose_name="Identyfikator - REGON")
    customer_type = models.CharField(max_length=15, choices=CUSTOMER_TYPE, default='enterprise')
    client_since = models.DateField()
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")

    def __str__(self):
         return f'{self.company_name}'

