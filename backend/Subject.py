from firebase_admin import firestore

class Subject:
    id_counter = 10000

    def __init__(self, name, spaces, levels):
        self.id = Subject.id_counter
        Subject.id_counter += 1
        self.name = name
        self.spaces = spaces
        self.levels = levels

    @staticmethod
    def create_subject(name, levels):
        # Create a new Location object
        new_subject = Subject(name=name, levels=levels)

        # Add the new location to the database
        db = firestore.client()
        location_ref = db.collection('Subjects').document(str(new_subject.id))
        location_ref.set(new_subject.__dict__)

    def delete_subject(subject_id):
        # Delete a subject from the database
        db = firestore.client()
        subject_ref = db.collection('Subjects').document(str(subject_id))
        subject_ref.delete()