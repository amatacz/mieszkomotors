from rest_framework import routers
from mieszkomotors import api_views 

app_name = "mieszkomotors"

router = routers.DefaultRouter()
router.register(r'car_events', api_views.CarEventsViewset)
router.register(r'insurance_events', api_views.InsuranceEventsViewset)
router.register(r'cars', api_views.CarViewset)