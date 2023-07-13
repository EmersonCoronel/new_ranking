from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from new_ranking.views import protected_view
#from .views import CustomLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/create_member/', views.create_member, name='create_member'),
    path('dashboard/create_location/', views.create_location, name='create_location'),
    path('dashboard/create_course/', views.create_course, name='create_course'),
    path('locations/', views.locations, name='locations'),
    path('members/', views.members, name='members'),
    path('trainers/', views.trainers, name='trainers'),
    path('collections/', views.collections, name='collections'),
]
