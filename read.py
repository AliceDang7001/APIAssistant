#If installation does work, but import won't go through then check for IDE issue
#IDE can be check by control+shift+P 
#After that search for interpreter and change it to the correct version
#In this way the files can be used for the install files

from googleapiclient.discovery import build 
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet. It is the part of the URL before and after the slash /. 
SAMPLE_SPREADSHEET_ID = 'Personal URL Needed'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sheet1!A1:F55").execute()
#values = result.get('values', [])
print(result)

