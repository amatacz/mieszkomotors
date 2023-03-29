from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render
import json

from django.urls import reverse_lazy
from django.views.generic import TemplateView

from mieszkomotors.models.events import CarEvent, InsuranceEvent

# class EventsListView(TemplateView):
#     model = CarEvent
#     template_name = "mieszkomotors/templates/calendar.html"

#     def car_events(request):
#         all_car_events = CarEvent.objects.all()

#         car_events_list = []
#         for i in all_car_events:
#             car_events_sub_list = {}
#             car_events_sub_list['car'] - i.car
#             car_events_sub_list['title'] = i.title
#             car_events_sub_list['start'] = i.start
#             car_events_sub_list['end'] = i.end
#             car_events_list.append(car_events_sub_list)

#         car_events_data = json.dumps(car_events_list)
#         return car_events_data
    
#     def insurance_events(request):
#         all_insurance_events = InsuranceEvent.objects.all()

#         insurance_events_list = []
#         for i in all_insurance_events:
#             insurance_events_sub_list = {}
#             insurance_events_sub_list['insurance'] - i.insurance
#             insurance_events_sub_list['title'] = i.title
#             insurance_events_sub_list['start'] = i.start
#             insurance_events_sub_list['end'] = i.end
#             insurance_events_list.append(insurance_events_sub_list)

#         insurance_events_data = json.dumps(insurance_events_list)
#         return insurance_events_data
    
#     def get_context_data(self, **kwargs):
#         context =  super().get_context_data(**kwargs)
#         context['car_events'] = self.car_events
#         context['insurance_events'] = self.insurance_events
#         return context
    
def car_events(request):
    all_car_events = CarEvent.objects.all()

    car_events_list = []
    for i in all_car_events:
        car_events_sub_list = {}
        car_events_sub_list['car'] - i.car
        car_events_sub_list['title'] = i.title
        car_events_sub_list['start'] = i.start
        car_events_sub_list['end'] = i.end
        car_events_list.append(car_events_sub_list)

    car_events_data = json.dumps(car_events_list)
    
    return JsonResponse(car_events_list, safe=False)

def insurance_events(request):
    all_insurance_events = InsuranceEvent.objects.all()

    insurance_events_list = []
    for i in all_insurance_events:
        insurance_events_sub_list = {}
        insurance_events_sub_list['insurance'] - i.insurance
        insurance_events_sub_list['title'] = i.title
        insurance_events_sub_list['start'] = i.start
        insurance_events_sub_list['end'] = i.end
        insurance_events_list.append(insurance_events_sub_list)

    insurance_events_data = json.dumps(insurance_events_list)

    return JsonResponse(insurance_events_list, safe=False)