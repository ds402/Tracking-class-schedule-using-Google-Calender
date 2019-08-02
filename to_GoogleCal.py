from __future__ import print_function
from apiclient import discovery
import httplib2  
from oauth2client import file, client, tools
import os
import oauth2client
from oauth2client import client
from oauth2client import tools
import datetime
import json

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'GCTT-IITBBS'

inputfile='timetable.json'
GMT_OFF = '+05:30'

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

days = {} # Days to number conversion
days["Monday"] = 0
days["Tuesday"] = 1
days["Wednesday"] = 2
days["Thursday"] = 3
days["Friday"] = 4
days["Saturday"] = 5


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def generate_time(next_day,lec_time):
    hours = (lec_time[0] + lec_time[1])
    minu = (lec_time[3] + lec_time[4])
    sec = (lec_time[6] + lec_time[7])
    actual_date = str(next_day.year) + '-' + str(next_day.month) + '-' + str(next_day.day)+ 'T' + hours +':'+ minu +':' + sec + GMT_OFF
    return actual_date


def get_credentials():
    """Gets valid user credentials from storage.
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.
    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

if __name__ == '__main__':
        
    creds = get_credentials()
    http = creds.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.now()
           
    with open(inputfile,'rb') as foo:
            data = json.load(foo)         
    for day in data:
         begin_day = next_weekday(now,days[day])
         for time in data[day]:
               event = {}
               lecSt = time['start']['lecSt']
               lecEd = time['end']['lecEd']
               event['summary'] = time['summary'] 
               event['description'] = time['description']
               event['location'] = time['location']
               event['start'] = {}
               event['start']['dateTime'] = generate_time(begin_day,lecSt)
               event['start']['timeZone'] = "Asia/Kolkata"
               event['end'] = {}
               event['end']['dateTime'] = generate_time(begin_day,lecEd)
               event['end']['timeZone'] = "Asia/Kolkata"
               event['recurrence'] = ['RRULE:FREQ=WEEKLY;UNTIL=20171130T230000Z']
               e = service.events().insert(calendarId='primary',sendNotifications=True, body=event).execute()
               print (event) 

    print ('Your event is added. ')



