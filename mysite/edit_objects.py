import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', "settings")
from new_ranking.models import Location
from new_ranking.models import Course
from new_ranking.models import Member
from new_ranking.models import Trainer

def editMemberFirstName(member, newFirstName):
    member.first_name = newFirstName
    member.save()
    return member

def editMemberLastName(member, newLastName):
    member.last_name = newLastName
    member.save()
    return member


def editMemberLocation(member, newLocation):
    member.location = newLocation
    member.save()
    return member

def editMemberPhoneNumber(member, newPhone_number):
    member.phone_number = newPhone_number
    member.save()
    return member

def editMemberEmail(member, newEmail):
    member.email = newEmail
    member.save()
    return member

def editMemberSpace(member, newSpace):
    member.space = newSpace
    member.save()
    return member

def editMemberGender(member, newGender):
    member.gender = newGender
    member.save()
    return member

def editMemberDateJoined(member, dateJoined):
    member.date_joined = dateJoined
    member.save()
    return member

def editMemberDateofBirth(member, dateOfBirth):
    member.date_of_birth = dateOfBirth
    member.save()
    return member

def editMemberPackage(member, newPackage):
    member.package = newPackage
    member.save()
    return member

def editMemberCourses(member, newCourses):
    member.courses = newCourses
    member.save()
    return member

def editMemberPassword(member, newPassword):
    member.password = newPassword
    member.save()
    return member

def editMemberTrainer(member, newTrainer):
    member.trainer = newTrainer
    member.save()
    return member

def editMemberRanking(member, newRanking):
    member.ranking = newRanking
    member.save()
    return member

def deleteMemeber(member):
    member.delete()

def editTrainerLocation(trainer, newLocation):
    trainer.location = newLocation
    trainer.save()
    return trainer

def editTrainerPhoneNumber(trainer, newPhoneNumber):
    trainer.phone_number = newPhoneNumber
    trainer.save()
    return trainer

def editTrainerEmail(trainer, newEmail):
    trainer.email = newEmail
    trainer.save()
    return trainer

def editTrainerSpace(trainer, newSpace):
    trainer.space = newSpace
    trainer.save()
    return trainer

def editLocationName(location, newLocationName):
    location.name = newLocationName
    location.save()
    return location


def deleteTrainer(trainer):
    trainer.delete()

def deleteCourse(course):
    course.delete()

def deleteCourseLevel(courseLevel):
    courseLevel.delete()

def deleteSpace(space):
    space.delete()