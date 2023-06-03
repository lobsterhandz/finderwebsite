from deta import Deta
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

# Instantiate Deta instance
deta = Deta("your_project_key")
# Access your base
db = deta.Base("your_base_name")

# Initiate FastAPI app
app = FastAPI()

# Define the profile data model
class Profile(BaseModel):
    name: str
    image: str
    url: str
    likes: int
    subscribers: int

@app.get("/api/profiles/{start}/{end}")
async def get_profiles(start: int, end: int):
    # Validating the input
    if start < 0 or end < 0 or start > end:
        raise HTTPException(status_code=400, detail="Invalid range provided.")
    try:
        profiles = list(db.fetch({}, limit=end))  # Fetching data from Deta Base
        if len(profiles) < end:
            raise HTTPException(status_code=404, detail="End of data reached.")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to fetch data from database.")
    return profiles[start:end]  # Returning the required profiles
