from __future__ import print_function

import json
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import sys

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses']


def main():
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    classId = {}
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])

    if __name__ == '__main__':
        if not courses:
            print('No courses found.')
        else:
            print('Courses:')
            for course in courses:
                print(course['name'], course['id'], course.get('courseState') and course['courseState'] == 'ACTIVE')
                classId.update({course['name']: course['id']})
    with open('courses.json', 'w') as outfile:
        outfile.write(json.dumps(results, indent=4))
    return classId

if __name__ == '__main__':
    main()
