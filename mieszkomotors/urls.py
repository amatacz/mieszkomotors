from django.urls import path, re_path

from .views import home, calendar, car, owner, user, insurance, events

urlpatterns = [
    path('', home.Home.as_view(), name='home'),

    # Cars urls
    path('car/create',
         car.CarCreate.as_view(),
         name='car_create'),
    path('car/update/<int:pk>',
         car.CarUpdate.as_view(),
         name='car_update'),
    path('car/delete/<int:pk>',
         car.CarDelete.as_view(),
         name='car_delete'),
    path('car/detail/<int:pk>',
         car.CarDetail.as_view(),
         name='car_detail'),
    path('car/list',
         car.CarList.as_view(),
         name='car_list'),

    # Car Owner urls
    path('car/<int:pk>/owner/create',
         car.CarOwnerCreate.as_view(),
         name='car_owner_create'),
    path('car/owner/<int:pk>/update',
         car.CarOwnerUpdate.as_view(),
         name='car_owner_update'),

    # All Customers list
    path('customers/list',
         owner.CustomersList.as_view(),
         name='customers_list'),

    # Individual Customers urls
    path('individual_customer/create',
         owner.IndividualCustomerCreate.as_view(),
         name='individual_customer_create'),
    path('individual_customer/update/<int:pk>',
         owner.IndividualCustomerUpdate.as_view(),
         name='individual_customer_update'),
    path('individual_customer/delete/<int:pk>',
         owner.IndividualCustomerDelete.as_view(),
         name='individual_customer_delete'),
    path('individual_customer/detail/<int:pk>',
         owner.IndividualCustomerDetail.as_view(),
         name='individual_customer_detail'),
    path('individual_customer/list/',
         owner.IndividualCustomersListView.as_view(),
         name='individual_customer_list'),

    # Self Employeed Customers urls
    path('self_employed_customer/create',
         owner.SelfEmployedCustomerCreate.as_view(),
         name='self_employed_customer_create'),
    path('self_employed_customer/update/<int:pk>',
         owner.SelfEmployedCustomerUpdate.as_view(),
         name='self_employed_customer_update'),
    path('self_employed_customer/delete/<int:pk>',
         owner.SelfEmployedCustomerDelete.as_view(),
         name='self_employed_customer_delete'),
    path('self_employed_customer/detail/<int:pk>',
         owner.SelfEmployedCustomerDetail.as_view(),
         name='selfemployed_customer_detail'),
    path('self_employed_customer/list/',
         owner.SelfEmployedCustomersListView.as_view(),
         name='self_employed_customer_list'),

    # Enterprise Customers urls
    path('enterprise_customer/create',
         owner.EnterpriseCustomerCreate.as_view(),
         name='enterprise_customer_create'),
    path('enterprise_customer/update/<int:pk>',
         owner.EnterpriseCustomerUpdate.as_view(),
         name='enterprise_customer_update'),
    path('enterprise_customer/delete/<int:pk>',
         owner.EnterpriseCustomerDelete.as_view(),
         name='enterprise_customer_delete'),
    path('enterprise_customer/detail/<int:pk>',
         owner.EnterpriseCustomerDetail.as_view(),
         name='enterprise_customer_detail'),
    path('enterprise_customer/list/',
         owner.EnterpriseCustomersListView.as_view(),
         name='enterprise_customer_list'),

    # Customer attachment urls
    path('customer_attachment/create/<str:customer_type>/<int:customer_id>',
         owner.CustomerAttachmentCreate.as_view(),
         name='customer_attachment_create'),
    path('customer_attachment_delete/<str:customer_type>/<int:customer_id>',
         owner.attachment_delete,
         name='customer_attachment_delete'),

    # Customer notes urls
    path('customer_note/create/<str:customer_type>/<int:customer_id>',
         owner.CustomerNoteCreate.as_view(),
         name='customer_note_create'),
    path('customer_note/update/<str:customer_type>/<int:customer_id>/<int:pk>',
         owner.CustomerNoteUpdate.as_view(),
         name='customer_note_update'),
    path('customer_note_delete/<str:customer_type>/<int:customer_id>',
         owner.note_delete,
         name='customer_note_delete'),
    path('customer_note_detail/<int:pk>',
         owner.CustomerNoteDetail.as_view(),
         name='customer_note_detail'),

    # Insurances urls
    path('insurance/create',
         insurance.InsuranceCreate.as_view(),
         name='insurance_create'),
    path('insurance/update/<int:pk>',
         insurance.InsuranceUpdate.as_view(),
         name='insurance_update'),
    path('insurance/delete/<int:pk>',
         insurance.InsuranceDelete.as_view(),
         name='insurance_delete'),
    path('insurance/detail/<int:pk>',
         insurance.InsuranceDetail.as_view(),
         name='insurance_detail'),
    path('insurance/list',
         insurance.InsuranceList.as_view(),
         name='insurance_list'),

    # GenericEvents urls
    path('events/create',
         events.GenericEventCreateView.as_view(),
         name='generic_event_create'),
    path('events/list',
         events.EventList.as_view(),
         name='events_list'),
    path('events/generic/detail/<int:pk>',
         events.GenericEventDetailView.as_view(),
         name="generic_event_detail"),
    path('events/generic/delete/<int:pk>',
         events.GenericEventDeleteView.as_view(),
         name="generic_event_delete"),
    path('events/generic/update/<int:pk>',
         events.GenericEventUpdateView.as_view(),
         name="generic_event_update"),

    # CarEvent urls
    path('events/car/detail/<int:pk>',
         events.CarEventDetailView.as_view(),
         name="car_event_detail"),

    # InsuranceEvent urls
    path('events/insurance/detail/<int:pk>',
         events.InsuranceEventDetailView.as_view(),
         name="insurance_event_detail"),

    # Calendar urls
    re_path(r'^calendar/$',
            calendar.CalendarView.as_view(),
            name='calendar'),

    # Login, logout urls
    path("login/",
         user.loginView.as_view(),
         name="login"),
    path("logout/",
         user.logoutView.as_view(),
         name="logout"),
]
