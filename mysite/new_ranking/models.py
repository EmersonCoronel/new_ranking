from django.db import models
from django.contrib.auth.models import User

class Package(models.Model):
    # Define Package model here
    pass

class Course(models.Model):
    name = models.CharField(max_length=200, default="Default Course Name")

class Level(models.Model):
    course = models.ForeignKey(Course, related_name='levels', on_delete=models.CASCADE)
    level = models.CharField(max_length=200, default="Default Level Data")

class Trainer(models.Model):
    first_name = models.CharField(max_length=100, default="Default First Name")
    last_name = models.CharField(max_length=100, default="Default Last Name")
    location = models.CharField(max_length=100, default="Default Location")
    phone_number = models.CharField(max_length=15, default="000-000-0000")
    email = models.EmailField(default="default@example.com")
    space = models.CharField(max_length=100, default="Default Space")
    gender = models.CharField(max_length=10, default="Other")
    date_joined = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField(default="2000-01-01")
    password = models.CharField(max_length=100, default="password")

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

class Member(models.Model):
    first_name = models.CharField(max_length=100, default="Default First Name")
    last_name = models.CharField(max_length=100, default="Default Last Name")
    location = models.CharField(max_length=100, default="Default Location")
    phone_number = models.CharField(max_length=15, default="000-000-0000")
    email = models.EmailField(default="default@example.com")
    space = models.CharField(max_length=100, default="Default Space")
    gender = models.CharField(max_length=10, default="Other")
    date_joined = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField(default="2000-01-01")
    package = models.ForeignKey(Package, on_delete=models.CASCADE, default=None, null=True)
    courses = models.ManyToManyField(Course)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, default=None, null=True)
    password = models.CharField(max_length=100, default="password")
    # You can create name as a property
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    ranking = models.IntegerField(null=True)
    # For past_rankings, you might want to create a separate model if it's going to be stored in the database

class PastRanking(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='past_rankings')
    ranking = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    
class Location(models.Model):
    name = models.CharField(max_length=200, default="Default Location Name")
    


class Space(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name= "spaces")
    name = models.CharField(max_length=100,default="Default Space Number")
    description = models.TextField()
    # Add more fields as per your requirements

    def __str__(self):
        return self.name