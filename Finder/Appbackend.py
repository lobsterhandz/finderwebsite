from flask import Flask, jsonify, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

app = Flask(__name__)

# Use your own scope and credentials
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open('your-google-sheet-name').sheet1  # replace with your Google Sheet name

@app.route('/profiles', methods=['GET'])
def get_profiles():
    all_data = sheet.get_all_records()
    df = pd.DataFrame(all_data)

    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=20, type=int)
    start = (page - 1) * per_page
    end = start + per_page
    data = df[start:end].to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
