import firebase_admin
import os
import objects
import Member
from firebase_admin import credentials, firestore
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError


# Connect to firebase
firebase_credentials = credentials.Certificate("backend/service_account_key.json")
firebase_admin.initialize_app(firebase_credentials)

# Create firestore database
db = firestore.client() # db is the database object

"""
get_classroom_credentials defines the scope for communicating between this venv and
classroom. Upon first run it will create a file called token.json which
contains user data for classroom. It returns the credentials required
to access google classroom information locally.
"""
def get_classroom_credentials():
    # Create access token and establish credentials for Google Classroom API
    SCOPES = [
    'https://www.googleapis.com/auth/classroom.courses.readonly',
    'https://www.googleapis.com/auth/classroom.rosters.readonly',
    'https://www.googleapis.com/auth/classroom.profile.emails',
    'https://www.googleapis.com/auth/classroom.profile.photos',
    'https://www.googleapis.com/auth/classroom.coursework.students',
    'https://www.googleapis.com/auth/classroom.coursework.me' ]

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('backend/classroom_token.json'):
        creds = Credentials.from_authorized_user_file('backend/classroom_token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'backend/classroom_credentials.json', SCOPES)
            flow.redirect_uri = 'http://localhost:8080'  # Set your fixed redirect URL here
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('backend/classroom_token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

"""
Recieves course information from google classroom,
creates student objects in firestore,
assigns basic information to each student
"""
def retrieve_classroom_data():
    # Create courses list
    courses = service.courses().list().execute()
    for course in courses['courses']:
        course_name = course['name']
        course_level = course['section']
        course_id = course['id']
        course_ref = db.collection('Courses').document(course_name + ' ' + course_level)
        course_ref.set({
            'Name': course_name,
            'Level': course_level,
            'ID': course_id
        })

        # Retrieve the students in the course
        students = []
        page_token = None
        while True:
            response = service.courses().students().list(courseId=course_id, pageSize=100, pageToken=page_token).execute()
            students.extend(response.get('students', []))
            page_token = response.get('nextPageToken')
            if not page_token:
                break

        # Create database object for each student
        for student in students:
            new_member = Member.Member(
                id=student['userId'],
                first_name=student['profile']['name']['givenName'],
                last_name=student['profile']['name']['familyName'],
                location=None,
                phone_number=None,
                email=student['profile']['emailAddress'],
                space=None,
                gender='Update',
                date_joined='Update',
                date_of_birth='Update',
                package='Update',
                courses=[course_ref],
                trainer='Update',
                password='N/A'
            )

            # Store the data in Firestore
            student_ref = db.collection('Member Information').document(str(new_member.id))
            student_ref.set(new_member.__dict__)

# Recieve classroom credntials
classroom_credentials = get_classroom_credentials()
# Build a service for accessing classroom
service = build('classroom', 'v1', credentials=classroom_credentials)

# Get classroom data and upload it to db
# retrieve_classroom_data()

# Create test student
Member.create_member(
    id="Test",
    first_name='John',
    last_name='Doe',
    location='New York',
    phone_number='1234567890',
    email='johndoe@example.com',
    space='Meeting Room',
    gender='Male',
    date_joined='2023-06-28',
    date_of_birth='1990-01-01',
    package='Gold',
    courses=['Course A', 'Course B'],
    trainer='Trainer A',
    password='password123'
)

