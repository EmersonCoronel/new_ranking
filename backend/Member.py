import firebase_admin
from firebase_admin import credentials, firestore

class Member:
    def __init__(self, id, first_name, last_name, location, phone_number, email, space, gender, date_joined,
                 date_of_birth, package, courses, trainer, password):
        self.id = id
        self.last_name = last_name
        self.location = location
        self.phone_number = phone_number
        self.email = email
        self.space = space
        self.gender = gender
        self.date_joined = date_joined
        self.date_of_birth = date_of_birth
        self.package = package
        self.courses = courses
        self.trainer = trainer
        self.password = password
        self.name = f"{first_name} {last_name}"
        self.ranking = None
        self.past_rankings = []

    @staticmethod
    def create_member(id, first_name, last_name, location, phone_number, email, space, gender, date_joined,
                    date_of_birth, package, courses, trainer, password):
        # Create a new Member object
        new_member = Member(id=id, first_name=first_name, last_name=last_name, location=location,
                            phone_number=phone_number, email=email, space=space, gender=gender,
                            date_joined=date_joined, date_of_birth=date_of_birth, package=package,
                            courses=courses, trainer=trainer, password=password)

        # Add the new member to the database
        db = firestore.client()
        member_ref = db.collection('Member Information').document(str(new_member.id))
        member_ref.set(new_member.__dict__)


    def update_ranking(member_id, ranking):
        # Update the ranking of a member in the database
        db = firestore.client()
        member_ref = db.collection('Member Information').document(str(member_id))
        # Get the member object to access its data in dictionary form
        member_obj = member_ref.get().to_dict()
        # Get the list of past rankings
        unfiltered_past_rankings = member_obj.get('past_rankings')
        past_rankings = list(filter(None, unfiltered_past_rankings))
        # Add the current ranking to past rankings
        if member_obj.get('ranking') != None:
            past_rankings.append(member_obj.get('ranking'))
        # Update the past and current rankings
        member_ref.update({'past_rankings' : past_rankings})
        member_ref.update({'ranking': ranking})
