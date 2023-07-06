import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from new_ranking.models import Location
from new_ranking.models import Course
from new_ranking.models import Member
from new_ranking.models import Trainer


def createLocation(locationName):
    newLocation = Location(name=locationName)
    newLocation.save()
    return newLocation

def createCourse(courseName):
    newCourse = Course(name=courseName)
    newCourse.save()
    return newCourse

def createMember(first_name, last_name, location, phone_number, email, space, gender, date_joined, date_of_birth, package, courses, trainer, password):
    newMember = Member()
    newMember.first_name = first_name
    newMember.last_name = last_name
    newMember.location = location
    newMember.phone_number = phone_number
    newMember.email = email
    newMember.space = space
    newMember.gender = gender
    newMember.date_joined = date_joined
    newMember.date_of_birth = date_of_birth
    newMember.package = package
    newMember.courses = courses
    newMember.trainer = trainer
    newMember.password = password
    newMember.save()
    return newMember

def createTrainer(user, first_name, last_name, location, phone_number, email, space, gender, date_joined, date_of_birth):
    newTrainer = Trainer()
    newTrainer.user = user
    newTrainer.first_name = first_name
    newTrainer.last_name = last_name
    newTrainer.location = location
    newTrainer.phone_number = phone_number
    newTrainer.email = email
    newTrainer.space = space
    newTrainer.gender = gender
    newTrainer.date_joined = date_joined
    newTrainer.date_of_birth = date_of_birth
    newTrainer.save()
    return newTrainer


print(createCourse("English 3"))