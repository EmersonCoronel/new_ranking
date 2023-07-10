from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth import views as auth_views

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    next_url = request.GET.get('next', 'dashboard')
    return render(request, 'login.html', {'next': next_url})

@login_required
def protected_view(request):
    return render(request, 'registration/login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CustomLoginView(auth_views.LoginView):
    success_url = reverse_lazy('dashboard')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)