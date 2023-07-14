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
def create_member(request):
    #newMember = Member()
    #newMember.save()=
    newMember = edit_objects.MemberFunctions.createMember()
    firstName = request.POST.get('first-name')
    if firstName != '':
        edit_objects.MemberFunctions.editMemberFirstName(newMember, firstName)
    lastName = request.POST.get('last-name')
    if lastName != '':
        edit_objects.MemberFunctions.editMemberLastName(newMember, lastName)
    location = request.POST.get('location')
    if location != '':
        edit_objects.MemberFunctions.editMemberLocation(newMember, location)
    phoneNumber = request.POST.get('phone-number')
    if phoneNumber != '':
        edit_objects.MemberFunctions.editMemberPhoneNumber(newMember, phoneNumber)
    email = request.POST.get('email')
    if email != '':
        edit_objects.MemberFunctions.editMemberEmail(newMember, email)
    space = request.POST.get('space')
    if space != '':
        edit_objects.MemberFunctions.editMemberSpace(newMember, space)
    gender = request.POST.get('gender')
    if gender != '':
        edit_objects.MemberFunctions.editMemberGender(newMember, gender)
    dateJoined = request.POST.get('date-joined')
    if dateJoined != '':
        edit_objects.MemberFunctions.editMemberDateJoined(newMember, dateJoined)
    dateOfBirth = request.POST.get('date-of-birth')
    if dateOfBirth != '':
        edit_objects.MemberFunctions.editMemberDateofBirth(newMember, dateOfBirth)
    package = request.POST.get('package')
    if package != '':
        edit_objects.MemberFunctions.editMemberPackage(newMember, package)
    courses = request.POST.get('courses')
    if courses != '':
        edit_objects.MemberFunctions.editMemberCourses(newMember, courses)
    trainer = request.POST.get('trainer')
    if trainer != '':
        edit_objects.MemberFunctions.editMemberTrainer(newMember, trainer)
    password = request.POST.get('password')
    if password != '':
        edit_objects.MemberFunctions.editMemberPassword(newMember, password)
    return redirect(reverse('members'))

@login_required
def create_location(request):
    edit_objects.LocationFunctions.createLocation()
    return redirect(reverse('dashboard'))

@login_required
def create_course(request):
    edit_objects.CourseFunctions.createCourse()
    return redirect(reverse('dashboard'))

@login_required
def protected_view(request):
    return render(request, 'registration/login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

@login_required
def locations(request):
    return render(request, 'dashboard/location.html')

@login_required
def members(request):
    return render(request, 'dashboard/members.html')

@login_required
def trainers(request):
    return render(request, 'dashboard/trainers.html')

@login_required
def collections(request):
    return render(request, 'dashboard/collections.html')