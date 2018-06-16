import httplib2
import os
import datetime
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import speedtest

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

def add_todo():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = 'your sheet id'
    connexion = test_connexion()

    
    list = [[ datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'), connexion['ping'], connexion['download']/1000000, connexion['upload']/1000000, connexion['server']['host'], "@"+connexion['server']['name'] + ", " + connexion['server']['country'] ]]
    resource = {
    "majorDimension": "ROWS",
    "values": list
}
    rangeName = 'A2:E'
    result = service.spreadsheets().values().append(spreadsheetId=spreadsheetId, range=rangeName,valueInputOption='USER_ENTERED', body=resource).execute()
    
    #ping_day
    day_Average(spreadsheetId, 'B2:B', service, 'K2')
    #up_day
    day_Average(spreadsheetId, 'C2:C', service, 'K3')
    #down_day
    day_Average(spreadsheetId, 'D2:D', service, 'K4')
    #ping_month
    month_Average(spreadsheetId, 'B2:B', service, 'L2')
    #up_month
    month_Average(spreadsheetId, 'C2:C', service, 'L3')
    #down_month
    month_Average(spreadsheetId, 'D2:D', service, 'L4')
    #last_ping
    last_Value(spreadsheetId, 'B2:B', service, 'I2')
    #last_Down
    last_Value(spreadsheetId, 'C2:C', service, 'I3')
    #last_Up
    last_Value(spreadsheetId, 'D2:D', service, 'I4')
    
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
                                   'mail_to_g_app.json')

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


def test_connexion():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    return s.results.dict()
    
    
def day_Average(spreadsheetId, rangeName_toAverage, service, rangeDestination):  
    n = 0
    i = 0
    average = 0
    rangeDateName = 'A2:A'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId,
                                             range=rangeDateName).execute()
    valuesdate = result.get('values', [])
    
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId,
                                             range=rangeName_toAverage).execute()
    valuesAverage =  result.get('values', [])
    
    for row in valuesdate:
        if row[0][:10] == datetime.datetime.now().strftime('%d/%m/%Y'):
            average = average + float(valuesAverage[i][0].replace(",", "."))
            n = n + 1.0
        i = i + 1
    value = {'values':[[average/n],]}
    result = service.spreadsheets().values().update(spreadsheetId=spreadsheetId,
                                    range=rangeDestination, valueInputOption='RAW', body=value).execute()


def month_Average(spreadsheetId, rangeName_toAverage, service, rangeDestination):  
    n = 0
    i = 0
    average = 0
    rangeDateName = 'A2:A'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId,
                                             range=rangeDateName).execute()
    valuesdate = result.get('values', [])
    
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId,range=rangeName_toAverage).execute()
    valuesAverage =  result.get('values', [])
    
    for row in valuesdate:
        if row[0][3:5] == datetime.datetime.now().strftime('%m'):
            average = average + float(valuesAverage[i][0].replace(",", "."))
            n = n + 1.0
        i = i + 1
    value = {'values':[[average/n],]}
    result = service.spreadsheets().values().update(spreadsheetId=spreadsheetId, range=rangeDestination, valueInputOption='RAW', body=value).execute()
    
    
def last_Value(spreadsheetId, rangeName_toAverage, service, rangeDestination):  
    rangeDateName = 'A2:A'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId,
                                             range=rangeDateName).execute()
    valuesdate = result.get('values', [])
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId,range=rangeName_toAverage).execute()
    valuesLast =  result.get('values', [])
    value = {'values':[[float(valuesLast[len(valuesdate)-1][0].replace(",", "."))],]}
    result = service.spreadsheets().values().update(spreadsheetId=spreadsheetId, range=rangeDestination, valueInputOption='RAW', body=value).execute()

if __name__ == '__main__':
    add_todo()
