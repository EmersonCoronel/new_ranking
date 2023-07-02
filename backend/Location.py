from firebase_admin import firestore

class Location:
    id_counter = 10000

    def __init__(self, name, spaces):
        self.id = Location.id_counter
        Location.id_counter += 1
        self.name = name
        self.spaces = spaces

    @staticmethod
    def create_location(name, spaces):
        # Create a new Location object
        new_location = Location(name=name, spaces=spaces)

        # Add the new location to the database
        db = firestore.client()
        location_ref = db.collection('Locations').document(str(new_location.id))
        location_ref.set(new_location.__dict__)
