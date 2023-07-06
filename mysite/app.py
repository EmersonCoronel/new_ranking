import os
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from new_ranking.models import Member, Level, Course

# Define the scopes of access on google classroom
def get_classroom_credentials():
    SCOPES = [
        'https://www.googleapis.com/auth/classroom.courses.readonly',
        'https://www.googleapis.com/auth/classroom.rosters.readonly',
        'https://www.googleapis.com/auth/classroom.profile.emails',
        'https://www.googleapis.com/auth/classroom.profile.photos',
        'https://www.googleapis.com/auth/classroom.coursework.students',
        'https://www.googleapis.com/auth/classroom.coursework.me'
    ]

    creds = None
    if os.path.exists('keys/classroom_token.json'):
        # Load credentials from file if it exists
        creds = Credentials.from_authorized_user_file('keys/classroom_token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh credentials if expired and a refresh token is available
            creds.refresh(Request())
        else:
            # Perform OAuth flow to get new credentials
            flow = InstalledAppFlow.from_client_secrets_file('keys/classroom_credentials.json', SCOPES)
            flow.redirect_uri = 'http://localhost:8080'
            creds = flow.run_local_server(port=8080)
        
        # Save the obtained credentials to a file
        with open('keys/classroom_token.json', 'w') as token:
            token.write(creds.to_json())
    
    return creds

def retrieve_classroom_data():
    # Retrieve courses from Google Classroom
    courses = service.courses().list().execute()
    
    # Initialize the IDs for courses and students
    current_course_id = 10000
    current_student_id = 10000
    
    for course in courses['courses']:
        # Create a Course object
        course_obj = Course.objects.create(
            name=course['name'],
            id=current_course_id
        )
        
        # Increment the course ID for the next iteration
        current_course_id += 1
        
        # Create a Level object associated with the course
        Level.objects.create(
            course=course_obj,
            level_data=course['section']
        )
        
        # Retrieve students in the course
        students = []
        page_token = None
        while True:
            response = service.courses().students().list(courseId=course['id'], pageSize=100, pageToken=page_token).execute()
            students.extend(response.get('students', []))
            page_token = response.get('nextPageToken')
            if not page_token:
                break
        
        for student in students:
            # Create a Member object for each student
            member_obj = Member.objects.create(
                id=current_student_id,
                first_name=student['profile']['name']['givenName'],
                last_name=student['profile']['name']['familyName'],
                email=student['profile']['emailAddress'],
            )
            
            # Associate the member with the course
            member_obj.courses.add(course_obj)
            
            # Increment the student ID for the next iteration
            current_student_id += 1

# Get Classroom credentials
classroom_credentials = get_classroom_credentials()

# Build Classroom service
service = build('classroom', 'v1', credentials=classroom_credentials)

# Retrieve and store Classroom data in the database
retrieve_classroom_data()
