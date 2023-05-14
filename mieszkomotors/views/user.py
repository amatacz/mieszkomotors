from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View

from mieszkomotors.forms import SignUpForm, LoginForm


# LogIn, LogOut, SignUp views

class signUp(View):
    form_class = SignUpForm
    template_name = 'registration/register.hmtl'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect('login')
        return render(request, self.template_name, {'form': form })


class loginView(View):
    form_class = LoginForm
    template_name = 'registration/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        if request.method == "POST":
            form = LoginForm(request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(
                        request, f"Zalogowałeś się jako {username}"
                    )
                    return redirect('home')
                else:
                    messages.error(request, "Błąd")
            else:
                messages.error(request, "Nieprawidłowa nazwa użytkownika lub hasło")
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})
    

class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')