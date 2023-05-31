

from gsheets import Sheets

# Use the JSON key file you downloaded
creds = 'C:\Users\----\AppData\gspread\service_account.json'

# Create a Sheets object
sheets = Sheets.from_files(creds)

# Open the Google Spreadsheet by its URL
spreadsheet = sheets.get('https://docs.google.com/spreadsheets/d/1NdEg_534I42LsNwZP3DNXJMSRtyTVO32PI2jAZDm5ag/edit?usp=sharing')

# Print the spreadsheet title and sheet names
print(f"Spreadsheet title: {spreadsheet.title}")
for sheet in spreadsheet.sheets:
    print(f"Sheet name: {sheet.name}")

# Test connection by retrieving and printing cell values
sheet = spreadsheet[0]
cell = sheet[1, 1]
print(f"Value in cell A1: {cell}")
