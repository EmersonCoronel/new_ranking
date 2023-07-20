from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm
from new_ranking.models import User
from new_ranking.models import Member
from new_ranking.models import Trainer
from new_ranking.models import Course
from new_ranking.models import Location
from django.db import models
from new_ranking.models import Space
from new_ranking.models import Admin

import edit_objects
from django.shortcuts import get_object_or_404, redirect

def admin_check(user):
    return user.is_authenticated and user.is_admin

def trainer_check(user):
    return user.is_authenticated and user.is_trainer

def member_check(user):
    return user.is_authenticated and user.is_member

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
            if user.is_admin:
                next_url = reverse('dashboard')  # replace 'dashboard' with the name of your dashboard view
            elif user.is_trainer:
                next_url = reverse('dashboard-trainer')  # replace 'dashboard-trainer' with the name of your trainer dashboard view
            else:
                next_url = reverse('dashboard-member')  # replace 'dashboard-member' with the name of your member dashboard view
            return redirect(next_url)
        else:
            print("Invalid")
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                user.is_trainer = True  # Set the user as an admin
                user.save()  # Save the change to the User object
                Trainer.objects.create(user=user)  # Create the corresponding Admin object
                login(request, user)
                if user.is_admin:
                    next_url = reverse('dashboard')  # replace 'dashboard' with the name of your dashboard view
                elif user.is_trainer:
                    next_url = reverse('dashboard-trainer')  # replace 'dashboard-trainer' with the name of your trainer dashboard view
                else:
                    next_url = reverse('dashboard-member')  # replace 'dashboard-member' with the name of your member dashboard view
                return redirect(next_url)
            else:
                messages.error(request, 'Authentication failed')
                return render(request, 'registration/signup.html', {'form': form})
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



class CustomLoginView(auth_views.LoginView):
    success_url = reverse_lazy('dashboard')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)

@login_required
@user_passes_test(admin_check)
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
    if dateJoined != '' and dateJoined == models.DateField:
        edit_objects.MemberFunctions.editMemberDateJoined(newMember, dateJoined)
    dateOfBirth = request.POST.get('date-of-birth')
    if dateOfBirth != '' and dateOfBirth == models.DateField:
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
@user_passes_test(admin_check)
def create_trainer(request):
    newTrainer = edit_objects.TrainerFunctions.createTrainer()
    firstName = request.POST.get('first-name')
    if firstName != '':
        edit_objects.TrainerFunctions.editTrainerFirstName(newTrainer, firstName)
    lastName = request.POST.get('last-name')
    if lastName != '':
        edit_objects.TrainerFunctions.editTrainerLastName(newTrainer, lastName)
    location = request.POST.get('location')
    if location != '':
        edit_objects.TrainerFunctions.editTrainerLocation(newTrainer, location)
    phoneNumber = request.POST.get('phone-number')
    if phoneNumber != '':
        edit_objects.TrainerFunctions.editTrainerPhoneNumber(newTrainer, phoneNumber)
    email = request.POST.get('email')
    if email != '':
        edit_objects.TrainerFunctions.editTrainerEmail(newTrainer, email)
    space = request.POST.get('space')
    if space != '':
        edit_objects.TrainerFunctions.editTrainerSpace(newTrainer, space)
    gender = request.POST.get('gender')
    if gender != '':
        edit_objects.TrainerFunctions.editTrainerGender(newTrainer, gender)
    dateJoined = request.POST.get('date-joined')
    if dateJoined != '' and dateJoined == models.DateField:
        edit_objects.TrainerFunctions.editTrainerDateJoined(newTrainer, dateJoined)
    dateOfBirth = request.POST.get('date-of-birth')
    if dateOfBirth != '' and dateOfBirth == models.DateField:
        edit_objects.TrainerFunctions.editTrainerDateofBirth(newTrainer, dateOfBirth)
    password = request.POST.get('password')
    if password != '':
        edit_objects.TrainerFunctions.editTrainerPassword(newTrainer, password)
    return redirect(reverse('trainers'))

@login_required
@user_passes_test(admin_check)
def create_location(request):
    newLocation = edit_objects.LocationFunctions.createLocation()
    location_name = request.POST.get('location-name')
    if location_name != '':
        edit_objects.LocationFunctions.editLocationName(newLocation, location_name)
    space = request.POST.get('space-num')
    if space != '':
        edit_objects.SpaceFunctions.createSpace(newLocation,space)
    return redirect(reverse('locations'))

@login_required
@user_passes_test(admin_check)
def add_space(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    if request.method == 'POST':
        space = request.POST.get('space')
        edit_objects.SpaceFunctions.createSpace(location, space)
        return redirect('locations')
    
@login_required
def protected_view(request):
    return render(request, 'registration/login.html')

@login_required
@user_passes_test(admin_check)
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
@user_passes_test(member_check)
def dashboardMember(request):
    return render(request, 'dashboard/dashboard-member.html')

@login_required
@user_passes_test(trainer_check)
def dashboardTrainer(request):
    return render(request, 'dashboard/dashboard-trainer.html')

@login_required
@user_passes_test(admin_check)
def profile(request):
    return render(request, 'registration/profile.html')

@login_required
@user_passes_test(member_check)
def profileMember(request):
    return render(request, 'registration/profile-member.html')

@login_required
@user_passes_test(trainer_check)
def profileTrainer(request):
    return render(request, 'registration/profile-trainer.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the old password is correct
        user = authenticate(username=request.user.username, password=old_password)
        if user is not None:
            # Check if the new passwords match
            if new_password == confirm_password:
                # Change the password
                user.set_password(new_password)
                user.save()
                # Update the user's session with the new password
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully!')
            else:
                messages.error(request, 'New passwords do not match.')
        else:
            messages.error(request, 'Old password is incorrect.')
    return redirect('profile')  # Replace 'profile' with the name of your profile view

@login_required
def logout_view(request):
    logout(request)
    return redirect('registration/login')  # Redirect to login page after logout

@login_required
@user_passes_test(admin_check)
def locations(request):
    locationCount = Location.objects.count()
    return render(request, 'dashboard/location.html', context={'count': locationCount, 'locations': Location.objects.all()})

@login_required
@user_passes_test(admin_check)
def delete_location(request, location_id):
    location = get_object_or_404(Location, id=location_id)
    if request.method == 'POST':
        location.delete()
        return redirect('locations')
    
@login_required
@user_passes_test(admin_check)
def delete_space(request, space_id):
    space = get_object_or_404(Space, id=space_id)
    if request.method == 'POST':
        space.delete()
        return redirect('locations')

@login_required
@user_passes_test(admin_check)
def members(request):
    memberCount = Member.objects.count()
    data = Member.objects.all()
    context={'count': memberCount, 'data':data}
    
    #for i, member in enumerate(Member.objects.all()):
        #context[str(i)] = (member.first_name, member.ranking, member.trainer, member.location)
    return render(request, 'dashboard/members.html', context)

@login_required
@user_passes_test(trainer_check)
def membersTrainer(request):
    memberCount = Member.objects.count()
    data = Member.objects.all()
    context={'count': memberCount, 'data':data}
    
    #for i, member in enumerate(Member.objects.all()):
        #context[str(i)] = (member.first_name, member.ranking, member.trainer, member.location)
    return render(request, 'dashboard/members-trainer.html', context)

@login_required
@user_passes_test(admin_check)
def trainers(request):
    trainerCount = Trainer.objects.count()
    return render(request, 'dashboard/trainers.html', context={'count': trainerCount, 'trainers': Trainer.objects.all()})

@login_required
@user_passes_test(admin_check)
def collections(request):
    collectionCount = Course.objects.count()
    return render(request, 'dashboard/collections.html', context={'count': collectionCount, 'collections': Course.objects.all()})

@login_required
@user_passes_test(admin_check)
def create_course(request):
    newCourse = edit_objects.CourseFunctions.createCourse()
    collection_name = request.POST.get('collection-name')
    edit_objects.CourseFunctions.editCourseName(newCourse, collection_name)
    newCourse.save()
    return redirect(reverse('collections'))

@login_required
@user_passes_test(admin_check)
def add_level(request, collection_id):
    collection = get_object_or_404(Course, id=collection_id)
    if request.method == 'POST':
        level = request.POST.get('level')
        edit_objects.LevelFunctions.createCourseLevel(collection, level)
        return redirect('collections')

@login_required
@user_passes_test(admin_check)
def delete_collection(request, collection_id):
    collection = get_object_or_404(Course, id=collection_id)
    if request.method == 'POST':
        collection.delete()
        return redirect('collections')