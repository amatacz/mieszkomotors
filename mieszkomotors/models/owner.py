from django.db import models

from .base import PublicationTracker, get_upload_path, get_upload_path_enterprise_owner


# class EnterpriseOwner(PublicationTracker):
#     ADDRES_PREFIXES = (
#          ("ul.", "ul."),
#          ("al.", "al."),
#          ("os.", "os."),
#          ("pl.", "pl.")
#         )
#     company_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=120, unique=True)
#     phone_number = models.CharField(max_length=12) # tu dodac walidację jakąś
#     address_prefix = models.CharField(max_length=3, choices=ADDRES_PREFIXES, default="ul.")
#     street = models.CharField(max_length=128, null=True, blank=True)
#     city = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=10)
#     building = models.CharField(max_length=10)
#     apartment = models.CharField(max_length=12)
#     nip = models.CharField(max_length=10, null=True, blank=True)
#     regon = models.CharField(max_length=10, null=True, blank=True)
#     client_since = models.DateField()
#     created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")

#     def __str__(self):
# 	    return f'{self.company_name}'

# class EnterpriseOwnerAttachment(PublicationTracker):
#     owner = models.ForeignKey(EnterpriseOwner, on_delete=models.CASCADE)
#     attachment = models.FileField(upload_to=get_upload_path_enterprise_owner)
#     created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")
    
#     def __str__(self):
# 	    return f'{self.attachment.name}'
    
# class EnterpriseOwnerNotes(PublicationTracker):
#     owner = models.ForeignKey(EnterpriseOwner, on_delete=models.CASCADE)
#     note = models.TextField(max_length=500)
#     created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")
    
#     def __str__(self):
# 	    return f'{self.note}'
    

# class SelfEmployedOwner(PublicationTracker):
#     ADDRES_PREFIXES = (
#         ("ul.", "ul."),
#         ("al.", "al."),
#         ("os.", "os."),
#         ("pl.", "pl.")
#         )
#     company_name = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=120, unique=True)
#     phone_number = models.CharField(max_length=12) # tu dodac walidację jakąś
#     address_prefix = models.CharField(max_length=3, choices=ADDRES_PREFIXES, default="ul.")
#     street = models.CharField(max_length=128, null=True, blank=True)
#     building = models.CharField(max_length=10)
#     apartment = models.CharField(max_length=12)
#     city = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=10)
#     nip = models.CharField(max_length=10, null=True, blank=True)
#     regon = models.CharField(max_length=10, null=True, blank=True)
#     client_since = models.DateField()
#     created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")

#     def __str__(self):
# 	    return f'{self.first_name} {self.last_name}'

# class SelfEmployedOwnerAttachment(PublicationTracker):
#     owner = models.ForeignKey(SelfEmployedOwner, on_delete=models.CASCADE)
#     attachment = models.FileField(upload_to=get_upload_path)
#     created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")

#     def __str__(self):
# 	    return f'{self.attachment.name}'

# class SelfEmployedOwnerNotes(PublicationTracker):
#     owner = models.ForeignKey(SelfEmployedOwner, on_delete=models.CASCADE)
#     note = models.TextField(max_length=500)
#     created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")

#     def __str__(self):
# 	    return f'{self.note}'

# class IndividualOwner(PublicationTracker):
#     ADDRES_PREFIXES = (
#          ("ul.", "ul."),
#          ("al.", "al."),
#          ("os.", "os."),
#          ("pl.", "pl.")
#         )
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=120, unique=True)
#     phone_number = models.CharField(max_length=12) # tu dodac walidację jakąś
#     address_prefix = models.CharField(max_length=3, choices=ADDRES_PREFIXES, default="ul.")
#     street = models.CharField(max_length=128, null=True, blank=True)
#     building = models.CharField(max_length=10)
#     apartment = models.CharField(max_length=12)
#     city = models.CharField(max_length=100)
#     zip_code = models.CharField(max_length=10)
#     pesel = models.CharField(max_length=11, null=True, blank=True)
#     client_since = models.DateField()
#     # customer = FK na customer, related name = 'individual_owner' 1t1 -> def null + uid, jako cos co bedzie uniq, "identifier", typ klienta choices
#     # sygnalem tworzyc customer z danymi wspolnymi 

#     def __str__(self):
# 	    return f'{self.first_name} {self.last_name}'

# class IndividualOwnerAttachment(PublicationTracker):
#     owner = models.ForeignKey(IndividualOwner, on_delete=models.CASCADE)
#     attachment = models.FileField(upload_to=get_upload_path, editable=True)
#     created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")

#     def __str__(self):
# 	    return f'{self.attachment.name}'

# class IndividualOwnerNotes(PublicationTracker):
#     owner = models.ForeignKey(IndividualOwner, on_delete=models.CASCADE)
#     note = models.TextField(max_length=500)
#     created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")

#     def __str__(self):
# 	    return f'{self.note}'
    


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
    phone_number = models.CharField(max_length=12) # tu dodac walidację jakąś
    address_prefix = models.CharField(max_length=3, choices=ADDRES_PREFIXES, default="ul.")
    street = models.CharField(max_length=128, null=True, blank=True)
    building = models.CharField(max_length=10)
    apartment = models.CharField(max_length=12)
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
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name= 'individual_owner', null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    pesel = models.CharField(max_length=11, unique=True, verbose_name="Identyfikator - PESEL")
    customer_type = models.CharField(max_length=15, choices=CUSTOMER_TYPE)
    client_since = models.DateField() 

    def __str__(self):
         return f'{self.first_name} {self.last_name}'

class SelfEmployedCustomer(ContactData):
    CUSTOMER_TYPE = (
          ('individual', 'IndividualCustomer'),
          ('selfemployed', 'SelfEmployedCustomer'),
          ('enterprise', 'EnterpriseCustomer')
    )

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name= 'self_employed_owner', null=True, blank=True)
    company_name = models.CharField(max_length=80)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    nip = models.CharField(max_length=10, verbose_name='NIP')
    regon = models.CharField(max_length=11, unique=True, verbose_name="Identyfikator - REGON")
    customer_type = models.CharField(max_length=15, choices=CUSTOMER_TYPE)
    client_since = models.DateField() 


    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.company_name}'
    
class EnterpriseCustomer(ContactData):
    CUSTOMER_TYPE = (
          ('individual', 'IndividualCustomer'),
          ('selfemployed', 'SelfEmployedCustomer'),
          ('enterprise', 'EnterpriseCustomer')
    )
    
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name= 'enterprise_owner', null=True, blank=True)
    company_name = models.CharField(max_length=100)
    nip = models.CharField(max_length=10, null=True, blank=True)
    regon = models.CharField(max_length=11, unique=True, verbose_name="Identyfikator - REGON")
    customer_type = models.CharField(max_length=15, choices=CUSTOMER_TYPE)
    client_since = models.DateField()
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE, default="auth.User")

    def __str__(self):
         return f'{self.company_name}'

