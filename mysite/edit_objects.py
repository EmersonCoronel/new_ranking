import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', "settings")
from new_ranking.models import Location
from new_ranking.models import Course
from new_ranking.models import Member
from new_ranking.models import Trainer

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