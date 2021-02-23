from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import sys
import Get_Class_Ids

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.me']


def main():
    global results
    classId = {'5 Symphonic  Band 2020-21 S2': '260795585673', 'Health': '254974568961',
               'Period 1 AP CS (A) Mr. Holcomb': '138766947580',
               'Period 3:AP Calculus AB': '130193944196',
               'AP GOPO': '127822934371', 'ERWC': '123501145589'}
    # Get_Class_Ids.main()#ts
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
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
    print("num of classes: ", len(classId))
    total_classwork=0
    for course in classId:
        results = service.courses().courseWork().list(courseId=classId[course], pageSize=10).execute()
        courseWork = results.get('courseWork', [])
        for i in courseWork:
            try:
                if i['state'] == 'PUBLISHED' and i['dueDate']['year'] >= 2021 and i['dueDate']['month'] >= 2 and i['dueDate']['day'] >= 23: #individwaly when the dates get compaired it messes up cuz 3/1  doesnt go though
                    print("Class:", course," HW:", i['title'], i['dueDate'])
                    total_classwork+=1
            except:
                pass
    print('total classwork: ', total_classwork)
    # sys.stdout = open('output.json', 'wt')
    # print(results) #.replace(',', ',\n'))


if __name__ == '__main__':
    main()
