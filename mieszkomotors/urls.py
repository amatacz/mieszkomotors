from django.urls import path, re_path
from .views import home, calendar, car, owner, user, insurance, events

urlpatterns = [
    path('', home.Home.as_view(), name='home'),

    # Cars urls
    path('car/create', car.CarCreate.as_view(), name='car_create'),
    path('car/update/<pk>', car.CarUpdate.as_view(), name='car_update'),
    path('car/delete/<pk>', car.CarDelete.as_view(), name='car_delete'),
    path('car/detail/<pk>', car.CarDetail.as_view(), name='car_detail'),
    path('car/list', car.CarList.as_view(), name='car_list'),

    # Car Owner urls
    path('car/<pk>/owner/create', car.CarOwnerCreate.as_view(), name='car_owner_create'),
    path('car/owner/<pk>/update', car.CarOwnerUpdate.as_view(), name='car_owner_update'),

    # All Customers list
    path('customers/list', owner.CustomersList.as_view(), name='customers_list'),

    # Individual Customers urls
    path('individual_customer/create', owner.IndividualCustomerCreate.as_view(), name='individual_customer_create'),
    path('individual_customer/update/<pk>', owner.IndividualCustomerUpdate.as_view(), name='individual_customer_update'),
    path('individual_customer/delete/<pk>', owner.IndividualCustomerDelete.as_view(), name='individual_customer_delete'),
    path('individual_customer/detail/<pk>', owner.IndividualCustomerDetail.as_view(), name='individual_customer_detail'),

     # Self Employeed Customers urls
    path('self_employed_customer/create', owner.SelfEmployedCustomerCreate.as_view(), name='self_employed_customer_create'),
    path('self_employed_customer/update/<pk>', owner.SelfEmployedCustomerUpdate.as_view(), name='self_employed_customer_update'),
    path('self_employed_customer/delete/<pk>', owner.SelfEmployedCustomerDelete.as_view(), name='self_employed_customer_delete'),
    path('self_employed_customer/detail/<pk>', owner.SelfEmployedCustomerDetail.as_view(), name='self_employed_customer_detail'),

     # Enterprise Customers urls
    path('enterprise_customer/create', owner.EnterpriseCustomerCreate.as_view(), name='enterprise_customer_create'),
    path('enterprise_customer/update/<pk>', owner.EnterpriseCustomerUpdate.as_view(), name='enterprise_customer_update'),
    path('enterprise_customer/delete/<pk>', owner.EnterpriseCustomerDelete.as_view(), name='enterprise_customer_delete'),
    path('enterprise_customer/detail/<pk>', owner.EnterpriseCustomerDetail.as_view(), name='enterprise_customer_detail'),

    # Customer attachment urls
    path('customer_attachment/create', owner.CustomerAttachmentCreate.as_view(), name='customer_attachment_create'),
    path('customer_attachment/update', owner.CustomerAttachmentUpdate.as_view(), name='customer_attachment_update'),
    path('customer_attachment_delete/<pk>', owner.CustomerAttachmentDelete.as_view(), name='customer_attachment_delete'),
    path('customer_attachment_detail/<pk>', owner.CustomerAttachmentDetail.as_view(), name='customer_attachment_detail'),
    
    # Customer notes urls
    path('customer_note/create', owner.CustomerNoteCreate.as_view(), name='customer_note_create'),
    path('customer_note/update', owner.CustomerNoteUpdate.as_view(), name='customer_note_update'),
    path('customer_note_delete/<pk>', owner.CustomerNoteDelete.as_view(), name='customer_note_delete'),
    path('customer_note_detail/<pk>', owner.CustomerNoteDetail.as_view(), name='customer_note_detail'),

    # Insurances urls
    path('insurance/create', insurance.InsuranceCreate.as_view(), name='insurance_create'),
    path('insurance/update/<pk>', insurance.InsuranceUpdate.as_view(), name='insurance_update'),
    path('insurance/delete/<pk>', insurance.InsuranceDelete.as_view(), name='insurance_delete'),
    path('insurance/detail/<pk>', insurance.InsuranceDetail.as_view(), name='insurance_detail'),
    path('insurance/list', insurance.InsuranceList.as_view(), name='insurance_list'),

    # GenericEvents urls
    path('events/create', events.GenericEventCreateView.as_view(), name='generic_event_create'),
    path('events/list', events.EventList.as_view(), name='events_list'),
    path('events/generic/detail/<pk>', events.GenericEventDetailView.as_view(), name = "generic_event_detail"),
    path('events/generic/delete/<pk>', events.GenericEventDeleteView.as_view(), name = "generic_event_delete"),
    path('events/generic/update/<pk>', events.GenericEventUpdateView.as_view(), name = "generic_event_update"),

    # CarEvent urls
    path('events/car/detail/<pk>', events.CarEventDetailView.as_view(), name = "car_event_detail"),

    # InsuranceEvent urls
    path('events/insurance/detail/<pk>', events.InsuranceEventDetailView.as_view(), name = "insurance_event_detail"),

    # Calendar urls
    re_path(r'^calendar/$', calendar.CalendarView.as_view(), name='calendar'),

    # Login, logout urls
    path("login/", user.loginView.as_view(), name="login"),
    path("logout/", user.logoutView.as_view(), name="logout"),

]