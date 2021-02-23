from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import sys

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly']


def main():
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    classId = {}
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists('token.pickle'):
        os.remove('token.pickle')
        """with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)"""
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])

    if __name__ == '__main__':
        if not courses:
            print('No courses found.')
        else:
            print('Courses:')
            for course in courses:
                try:
                    print(course['name'], course['id'], course['courseState'] == 'ACTIVE')
                    classId.update({course['name']: course['id']})
                except:
                    print('no section')
    print(classId)
    sys.stdout = open('classes.txt', 'wt')
    print(str(results).replace(',', ',\n'))
    os.remove('token.pickle')
    return classId


if __name__ == '__main__':
    main()
