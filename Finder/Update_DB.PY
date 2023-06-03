from deta import Deta
import csv

# Instantiate Deta instance
deta = Deta("your_project_key")
# Access your base
db = deta.Base("your_base_name")

# Open the CSV file and read the data
with open('path_to_your_file.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Construct a unique key. Here, we're assuming the username is unique.
        # If the unique identifier is a composite of multiple fields, concatenate them.
        key = row['username']

        # Fetch the item from the base by its key
        item = db.get(key)
        # If item does not exist, put it in the base
        if not item:
            db.put({**row, 'key': key})

