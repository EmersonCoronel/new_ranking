import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from new_ranking.models import Location
from new_ranking.models import Course
from new_ranking.models import Member
from new_ranking.models import Trainer
from new_ranking.models import Level
from new_ranking.models import Space
from django.contrib.auth.models import User


def createLocation(locationName):
    newLocation = Location(name=locationName)
    newLocation.save()
    return newLocation

def createSpace(spaceLocation):
    newSpace = Space(location = spaceLocation)
    newSpace.save()
    return newSpace

def createCourse(courseName):
    newCourse = Course(name=courseName)
    newCourse.save()
    return newCourse

def createLevel(levelCourse):
    newLevel = Level(course=levelCourse)
    newLevel.save()
    return newLevel

def createMember():
    newMember = Member()
    newMember.save()
    return newMember

def createTrainer(trainerUser):
    newTrainer = Trainer(user = trainerUser)
    newTrainer.save()
    return newTrainer

