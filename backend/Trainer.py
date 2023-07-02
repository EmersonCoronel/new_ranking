from firebase_admin import firestore

# Trainer class
class Trainer:
    def __init__(self, id, first_name, last_name, location, phone_number, email, space, gender, date_joined,
                 date_of_birth, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.phone_number = phone_number
        self.email = email
        self.space = space
        self.gender = gender
        self.date_joined = date_joined
        self.date_of_birth = date_of_birth
        self.password = password

    @staticmethod
    def create_trainer(id, first_name, last_name, location, phone_number, email, space, gender, date_joined,
                      date_of_birth, password):
        # Create a new Trainer object
        db = firestore.client()
        new_trainer = Trainer(id=id, first_name=first_name, last_name=last_name, location=location,
                              phone_number=phone_number, email=email, space=space, gender=gender,
                              date_joined=date_joined, date_of_birth=date_of_birth, password=password)

        # Add the new trainer to the database
        trainer_ref = db.collection('Trainers').document(str(new_trainer.id))
        trainer_ref.set(new_trainer.__dict__)