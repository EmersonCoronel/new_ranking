from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from new_ranking.models import Member
from new_ranking.models import Location
from new_ranking.models import Course
from django.http import HttpResponse
import edit_objects

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def login_view(request):
    if request.method == 'POST':
        userUsername = request.POST['username']
        userPassword = request.POST['password']
        try:
            user = User.objects.get(username = userUsername)
            print("User exists")
        except User.DoesNotExist:
            print("User does not exist")
        user = authenticate(request, username=userUsername, password=userPassword)
        if user is not None:
            print("Valid")
            login(request, user)
            next_url = request.POST.get('next', 'dashboard')
            return redirect(next_url)
        else:
            print("Invalid")
            messages.error(request, 'Invalid username or password.')
    next_url = request.GET.get('next', 'dashboard/dashboard.html')
    return render(request, 'registration/login.html', {'next': next_url})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print('valid form')
            agree_to_terms = form.cleaned_data.get('agree_to_terms')
            if not agree_to_terms:
                messages.error(request, 'You must agree to the terms to sign up')
                return render(request, 'registration/signup.html', {'form': form})
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(reverse('dashboard'))
            else:
                messages.error(request, 'Authentication failed')
                return render(request, 'registration/signup.html', {'form': form})
        else:
            print('invalid form')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def protected_view(request):
    return render(request, 'registration/login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')