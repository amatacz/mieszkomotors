from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.CalendarView.as_view(), name='home'),

    # Cars urls
    path('car/create', views.CarCreate.as_view(), name='car_create'),
    path('car/update/<pk>', views.CarUpdate.as_view(), name='car_update'),
    path('car/delete/<pk>', views.CarDelete.as_view(), name='car_delete'),
    path('car/detail/<pk>', views.CarDetail.as_view(), name='car_detail'),
    path('car/list', views.CarList.as_view(), name='car_list'),

    # Owners urls
    path('owner/create', views.OwnerCreate.as_view(), name='owner_create'),
    path('owner/update/<pk>', views.OwnerUpdate.as_view(), name='owner_update'),
    path('owner/delete/<pk>', views.OwnerDelete.as_view(), name='owner_delete'),
    path('owner/detail/<pk>', views.OwnerDetail.as_view(), name='owner_detail'),
    path('owner/list', views.OwnerList.as_view(), name='owner_list'),

    # Insurances urls
    path('insurance/create', views.InsuranceCreate.as_view(), name='insurance_create'),
    path('insurance/update/<pk>', views.InsuranceUpdate.as_view(), name='insurance_update'),
    path('insurance/delete/<pk>', views.InsuranceDelete.as_view(), name='insurance_delete'),
    path('insurance/detail/<pk>', views.InsuranceDetail.as_view(), name='insurance_detail'),
    path('insurance/list', views.InsuranceList.as_view(), name='insurance_list'),

    # Calendar urls
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),

]