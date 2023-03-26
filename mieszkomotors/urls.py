from django.urls import path, re_path
from .views import home, calendar, car, owner

urlpatterns = [
     path('', home.Home.as_view(), name='home'),

     # Cars urls
     path('car/create', car.CarCreate.as_view(), name='car_create'),
     path('car/update/<pk>', car.CarUpdate.as_view(), name='car_update'),
     path('car/delete/<pk>', car.CarDelete.as_view(), name='car_delete'),
     path('car/detail/<pk>', car.CarDetail.as_view(), name='car_detail'),
     path('car/list', car.CarList.as_view(), name='car_list'),

     # Individual Owners urls
    path('owner/create', owner.IndividualOwnerCreate.as_view(), name='owner_create'),
    path('owner/update/<pk>', owner.IndividualOwnerUpdate.as_view(), name='owner_update'),
    path('owner/delete/<pk>', owner.IndividualOwnerDelete.as_view(), name='owner_delete'),
    path('owner/detail/<pk>', owner.IndividualOwnerDetail.as_view(), name='owner_detail'),
    path('owner/list', owner.OwnersList.as_view(), name='owner_list'),

    # Individual Owners Attachment urls
    path('owner/<pk>/attachment/create', owner.IndividualOwnerAttachmentCreate.as_view(), name='owner_attachment_create'),
    path('owner/<pk>/attachment/update', owner.IndividualOwnerAttachmentUpdate.as_view(), name='owner_attachment_update'),
    path('owner/<pk>/attachment/delete', owner.IndividualOwnerAttachmentDelete.as_view(), name='owner_attachment_delete'),
    path('owner/<pk>/attachment/detail', owner.IndividualOwnerAttachmentDetail.as_view(), name='owner_attachment_detail'),
    path('owner/<pk>/attachment/list', owner.IndividualOwnerAttachmentList.as_view(), name='owner_attachment_list'),

    # Individual Owners Notes urls
    path('owner/<pk>/note/create', owner.IndividualOwnerNotesCreate.as_view(), name='owner_note_create'),
    path('owner/<pk>/note/update/<note_pk>', owner.IndividualOwnerNotesUpdate.as_view(), name='owner_note_update'),
    path('owner/<pk>/note/delete/<note_pk>', owner.IndividualOwnerNotesDelete.as_view(), name='owner_note_delete'),
    path('owner/<pk>/note/detail/<note_pk>', owner.IndividualOwnerNotesDetail.as_view(), name='owner_note_detail'),
    path('owner/<pk>/note/list', owner.IndividualOwnerNotesList.as_view(), name='owner_note_list'),

         # Self Employeed Owners urls
    path('self_employed_owner/create', owner.SelfEmployedOwnerCreate.as_view(), name='self_employed_owner_create'),
    path('self_employed_owner/update/<pk>', owner.SelfEmployedOwnerOwnerUpdate.as_view(), name='self_employed_owner_update'),
    path('self_employed_owner/delete/<pk>', owner.SelfEmployedOwnerOwnerDelete.as_view(), name='self_employed_owner_delete'),
    path('self_employed_owner/detail/<pk>', owner.SelfEmployedOwnerDetail.as_view(), name='self_employed_owner_detail'),
    path('self_employed_owner/list', owner.OwnersList.as_view(), name='owner_list'),

    # Self Employeed Owners Attachment urls
    path('self_employed_owner/<pk>/attachment/create', owner.SelfEmployedOwnerAttachmentCreate.as_view(), name='self_employed_owner_attachment_create'),
    path('self_employed_owner/<pk>/attachment/update', owner.SelfEmployedOwnerAttachmentUpdate.as_view(), name='self_employed_owner_attachment_update'),
    path('self_employed_owner/<pk>/attachment/delete', owner.SelfEmployedOwnerAttachmentDelete.as_view(), name='self_employed_owner_attachment_delete'),
    path('self_employed_owner/<pk>/attachment/detail', owner.SelfEmployedOwnerAttachmentDetail.as_view(), name='self_employed_owner_attachment_detail'),
    path('self_employed_owner/<pk>/attachment/list', owner.SelfEmployedOwnerAttachmentList.as_view(), name='self_employed_owner_attachment_list'),

    # Self Employeed Owners Notes urls
    path('self_employed_owner/<pk>/note/create', owner.SelfEmployedOwnerNotesCreate.as_view(), name='self_employed_owner_note_create'),
    path('self_employed_owner/<pk>/note/update/<note_pk>', owner.SelfEmployedOwnerNotesUpdate.as_view(), name='self_employed_owner_note_update'),
    path('self_employed_owner/<pk>/note/delete/<note_pk>', owner.SelfEmployedOwnerNotesDelete.as_view(), name='self_employed_owner_note_delete'),
    path('self_employed_owner/<pk>/note/detail/<note_pk>', owner.SelfEmployedOwnerNotesDetail.as_view(), name='self_employed_owner_note_detail'),
    path('self_employed_owner/<pk>/note/list', owner.SelfEmployedOwnerNotesList.as_view(), name='self_employed_owner_note_list'),


#     # Insurances urls
#     path('insurance/create', views.InsuranceCreate.as_view(), name='insurance_create'),
#     path('insurance/update/<pk>', views.InsuranceUpdate.as_view(), name='insurance_update'),
#     path('insurance/delete/<pk>', views.InsuranceDelete.as_view(), name='insurance_delete'),
#     path('insurance/detail/<pk>', views.InsuranceDetail.as_view(), name='insurance_detail'),
#     path('insurance/list', views.InsuranceList.as_view(), name='insurance_list'),

     # Calendar urls
     re_path(r'^calendar/$', calendar.CalendarView.as_view(), name='calendar'),

#     # Login, logout urls
#     path("login/", views.loginView.as_view(), name="login"),
#     path("logout/", views.logoutView.as_view(), name="logout"),

]