import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from new_ranking.models import Location
from new_ranking.models import Space
from new_ranking.models import Course
from new_ranking.models import Member
from new_ranking.models import Trainer
from new_ranking.models import Level

from new_ranking.models import Package
from new_ranking.models import PastRanking

class MemberFunctions:

    def createMember():
        newMember = Member()
        newMember.save()
        return newMember
    
    def deleteMemeber(member):
        member.delete()

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
        packages = Package.objects.all()
        if newPackage in packages:
            member.package = newPackage
            member.save()
        return member

    def editMemberCourses(member, newCourses):
        courses = Course.objects.all()
        if newCourses in courses:
            member.courses.set(newCourses)
            member.save()
        return member
    
    def editMemberTrainer(member, newTrainer):
        trainers = Trainer.objects.all()
        if newTrainer in trainers:
            member.trainer = newTrainer
            member.save()
        return member

    def editMemberPassword(member, newPassword):
        member.password = newPassword
        member.save()
        return member

    def editMemberRanking(member, newRanking):
        member.ranking = newRanking
        member.save()
        return member



class TrainerFunctions:

    def createTrainer():
        newTrainer = Trainer()
        newTrainer.save()
        return newTrainer
    
    def deleteTrainer(trainer):
        trainer.delete()

    def editTrainerFirstName(trainer, newFirstName):
        trainer.first_name = newFirstName
        trainer.save()
        return trainer

    def editTrainerLastName(trainer, newLastName):
        trainer.last_name = newLastName
        trainer.save()
        return trainer

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
    
    def editTrainerGender(trainer, newGender):
        trainer.gender = newGender
        trainer.save()
        return trainer

    def editTrainerDateJoined(trainer, dateJoined):
        trainer.date_joined = dateJoined
        trainer.save()
        return trainer

    def editTrainerDateofBirth(trainer, dateOfBirth):
        trainer.date_of_birth = dateOfBirth
        trainer.save()
        return trainer
    
    def editTrainerPassword(trainer, password):
        trainer.password = password
        trainer.save()
        return trainer
    
class PackageFunctions:

    def createPackage(packagePlan):
        newPackage = Package(plan = packagePlan)
        newPackage.save()
        return newPackage
    
    def deletePackage(package):
        package.delete()

class CourseFunctions:

    def createCourse(courseName="Default course name"):
        newCourse = Course(name=courseName)
        newCourse.save()
        return newCourse
    
    def editCourseName(course, newCourseName):
        course.name = newCourseName
        course.save()
        return course
    
    def deleteCourse(course):
        course.delete()

class PastRankingFunctions:
    pass

class LevelFunctions:

    def createCourseLevel(course, levelName):
        newLevel = Level(course=course, level=levelName)
        newLevel.save()
        return newLevel

    def deleteCourseLevel(courseLevel):
        courseLevel.delete()

class LocationFunctions:

    def createLocation():
        newLocation = Location()
        newLocation.save()
        return newLocation

    def deleteLocation(location):
        location.delete()

    def editLocationName(location, newLocationName):
        location.name = newLocationName
        location.save()
        return location
    
    # def editLocationSpace(location, newSpace):
    #     location.space = newSpace
    #     location.save()
    #     return location


class SpaceFunctions:

    def createSpace(location, spaceNumber = "Default Space Number"):
        newSpace = Space(location = location, name=spaceNumber)
        newSpace.save()
        return newSpace
    
    def deleteSpace(spaceNumber):
        spaceNumber.delete()
        




