from googleapiclient.discovery import build 
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet. It is the part of the URL before and after the slash /. 
SAMPLE_SPREADSHEET_ID = 'Your Own URL'


service = build('sheets', 'v4', credentials=creds)

# Call/Read the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sheet1!A1:F55").execute() # Set Up the Range
values = result.get('values', []) 

# print(result) # Print the entire result and range code included
print(values) # Print just the spreedshet as a simple list

aoa = [["1/1/2020",4000],["4/4/2020",3000],["7/12/2020",2000]]

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sheet2!A1", valueInputOption="USER_ENTERED", body={"values":aoa}).execute()
