from __future__ import print_function
from apiclient import discovery
import httplib2  
from oauth2client import file, client, tools
import os
import oauth2client
from oauth2client import client
from oauth2client import tools

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'GCTT-IITBBS'

GMT_OFF = '+05:30'

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


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

          
    EVENT = {
            'summary': 'GOOGLE CALENDER using Python',
            'location': 'Your Sweet Home',
            'description': 'I am learning PYTHON',
            'start':  {'dateTime': '2017-09-29T08:00:00%s' % GMT_OFF},
            'end':    {'dateTime': '2017-09-29T10:00:00%s' % GMT_OFF},
        }

    e = service.events().insert(calendarId='primary',
                sendNotifications=True, body=EVENT).execute()

    print ('Your event is added. ')



