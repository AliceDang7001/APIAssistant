from googleapiclient.discovery import build 
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet. It is the part of the URL before and after the slash /. 
SAMPLE_SPREADSHEET_ID = '1ejW5oh5fE_e75-UdKtBJYVGikzC_8Bsn7n2l7LtxkbI'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sheet1!A1:F55").execute()
#values = result.get('values', [])
print(result)

