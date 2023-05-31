import gspread
from oauth2client.service_account import ServiceAccountCredentials
from deta import Deta

# Use your own scope, credentials, and sheet details here
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('path_to_your_credentials_file.json', scope)
client = gspread.authorize(creds)

# Open the spreadhseet
sheet = client.open('Your_Sheet_Name').sheet1

# Get all records of the data
data = sheet.get_all_records()

# Instantiate the Deta object with your project key
deta = Deta("project_key")

# Access your base
base = deta.Base("base_name")

# Iterate over the data and insert each record into the base
for record in data:
    base.put(record)
