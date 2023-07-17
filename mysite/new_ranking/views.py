from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from new_ranking.models import Member
from new_ranking.models import Trainer
from new_ranking.models import Course
from new_ranking.models import Location
import edit_objects
from django.shortcuts import get_object_or_404, redirect


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

class CustomLoginView(auth_views.LoginView):
    success_url = reverse_lazy('dashboard')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password.')
        return super().form_invalid(form)

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
    if dateJoined != '':
        edit_objects.TrainerFunctions.editTrainerDateJoined(newTrainer, dateJoined)
    dateOfBirth = request.POST.get('date-of-birth')
    if dateOfBirth != '':
        edit_objects.TrainerFunctions.editTrainerDateofBirth(newTrainer, dateOfBirth)
    password = request.POST.get('password')
    if password != '':
        edit_objects.TrainerFunctions.editTrainerPassword(newTrainer, password)
    return redirect(reverse('trainers'))

@login_required
def create_location(request):
    newLocation = edit_objects.LocationFunctions.createLocation()
    location_name = request.POST.get('location-name')
    if location_name != '':
        edit_objects.LocationFunctions.editLocationName(newLocation, location_name)
    space = request.POST.get('space-num')
    if space != '':
        edit_objects.LocationFunctions.editLocationSpace(newLocation, space)
    return redirect(reverse('locations'))

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

def logout_view(request):
    logout(request)
    return redirect('registration/login')  # Redirect to login page after logout

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

@login_required
def locations(request):
    locationCount = Location.objects.count()
    return render(request, 'dashboard/location.html', context={'count': locationCount, 'locations': Location.objects.all()})

@login_required
def members(request):
    memberCount = Member.objects.count()
    data = Member.objects.all()
    context={'count': memberCount, 'data':data}
    
    #for i, member in enumerate(Member.objects.all()):
        #context[str(i)] = (member.first_name, member.ranking, member.trainer, member.location)
    return render(request, 'dashboard/members.html', context)

@login_required
def trainers(request):
    trainerCount = Trainer.objects.count()
    return render(request, 'dashboard/trainers.html', context={'count': trainerCount, 'trainers': Trainer.objects.all()})

@login_required
def collections(request):
    collectionCount = Course.objects.count()
    return render(request, 'dashboard/collections.html', context={'count': collectionCount, 'collections': Course.objects.all()})

@login_required
def create_course(request):
    newCourse = edit_objects.CourseFunctions.createCourse()
    collection_name = request.POST.get('collection-name')
    edit_objects.CourseFunctions.editCourseName(newCourse, collection_name)
    newCourse.save()
    return redirect(reverse('collections'))

@login_required
def add_level(request, collection_id):
    collection = get_object_or_404(Course, id=collection_id)
    if request.method == 'POST':
        level = request.POST.get('level')
        edit_objects.LevelFunctions.createCourseLevel(collection, level)
        return redirect('collections')

@login_required
def delete_collection(request, collection_id):
    collection = get_object_or_404(Course, id=collection_id)
    if request.method == 'POST':
        collection.delete()
        return redirect('collections')