import firebase_admin
import os
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

# Recieve classroom credntials
classroom_credentials = get_classroom_credentials()
# Build a service for accessing classroom
service = build('classroom', 'v1', credentials=classroom_credentials)

"""
Recieves course information from google classroom,
creates student objects in firestore,
assigns basic information to each student
"""
def retrieve_classroom_data():
    # Create courses list
    courses = service.courses().list().execute()
    for course in courses['courses']:
        course_id = course['id']
        course_name = course['name']

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
            student_id = student['userId']
            student_name = student['profile']['name']['fullName']
            trainer = 'Mikal Hagos' # Need to figure out how to automate

            # Store the data in Firestore
            student_ref = db.collection('Students').document(student_name)
            student_ref.set({
                'Classroom ID': student_id,
                'Courses': [course_name + ' ' + course['section']],
                'Trainer': trainer,
                'Motivation': 0,
                'Behavior': 0,
                'Coursework Difficulty': 0,
                'Challenge': 0,
                'Progress': 0
            })

retrieve_classroom_data()