from rest_framework import routers
from mieszkomotors import api_views 

app_name = "mieszkomotors"

router = routers.DefaultRouter()
router.register(r'car_events', api_views.CarEventsViewset)
router.register(r'insurance_events', api_views.InsuranceEventsViewset)
router.register(r'cars', api_views.CarViewset)
router.register(r'car_owners', api_views.CarOwnerViewset)
router.register(r'insurances', api_views.InsuranceViewset)
router.register(r'customers', api_views.CustomerViewset)
router.register(r'individual_customers', api_views.IndividualCustomerViewset)
router.register(r'self_employed_customers', api_views.SelfEmployedCustomerViewset)
router.register(r'enterprise_customers', api_views.EnterpriseCustomerViewset)