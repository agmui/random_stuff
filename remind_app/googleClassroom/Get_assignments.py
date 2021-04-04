from __future__ import print_function

import json
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import Get_Class_Ids
import datetime

# If modifying these scopes, delete the file token.pickle.

SCOPES = ['https://www.googleapis.com/auth/classroom.coursework.me']

def fun(d, name1, name2):
    if name1 in d:
        yield d[name1]
    if name2 in d:
        yield d[name2]
    for k in d:
        if isinstance(d[k], list):
            for i in d[k]:
                for j in fun(i, name1, name2):
                    yield j
def main():
    classId = {'5 Symphonic  Band 2020-21 S2': '260795585673', 'Health': '254974568961',
               'Period 1 AP CS (A) Mr. Holcomb': '138766947580',
               'Period 3:AP Calculus AB': '130193944196',
               'AP GOPO': '127822934371', 'ERWC': '123501145589'}

    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first

    # If there are no (valid) credentials available, let the user log in.
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)


    service = build('classroom', 'v1', credentials=creds)

    # Call the Classroom API
    print("num of classes: ", len(classId))
    total={}
    for course in classId:
        results = service.courses().courseWork().list(courseId=classId[course], pageSize=10).execute()
#        total[course] = results
        for i in list(fun(results, 'title', 'dueDate')):
            if isinstance(i, dict):
                HW_date = datetime.datetime(i['year'], i['month'], i['day'])
                if HW_date > datetime.datetime.now():
                    print(i)
                    total[course] = results
    with open('output.json', 'w') as outfile:
        outfile.write(json.dumps(total))


if __name__ == '__main__':
    main()
