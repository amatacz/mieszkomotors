from django.shortcuts import render, redirect
from django.views.generic import View


# Home
class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('calendar')
        return render(request, 'home.html')
