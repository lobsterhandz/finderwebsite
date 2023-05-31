from deta import Deta
from fastapi import FastAPI
from typing import List

# Initialize the Deta Base
deta = Deta("project_key")  # replace "project_key" with your actual project key
db = deta.Base("base_name")  # replace "base_name" with your actual base name

app = FastAPI()

@app.get("/profiles", response_model=List[dict])
async def get_profiles(skip: int = 0, limit: int = 100):
    profiles = db.fetch({}, skip=skip, limit=limit)
    return list(profiles)

