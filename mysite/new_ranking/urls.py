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
    path('members/create_member/', views.create_member, name='create_member'),
    path('trainers/create_trainer/', views.create_trainer, name='create_trainer'),
    path('locations/create_location/', views.create_location, name='create_location'),
    path('collections/create_course/', views.create_course, name='create_course'),
    path('delete_collection/<int:collection_id>/', views.delete_collection, name='delete_collection'),
    path('change_password/', views.change_password, name='change_password'),
    path('logout/', views.logout_view, name='logout'),
    path('locations/', views.locations, name='locations'),
    path('members/', views.members, name='members'),
    path('trainers/', views.trainers, name='trainers'),
    path('collections/', views.collections, name='collections'),
]
