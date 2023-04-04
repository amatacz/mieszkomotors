from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from mieszkomotors.models.car import Car

# Calendar Views
class CalendarView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'calendar.html'
