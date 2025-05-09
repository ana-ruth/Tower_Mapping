from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile

from towerProcessor import *

app = FastAPI()


@app.get("/")
async def root():
    return {"ping": "pong"}

@app.get("/api/data")
def get_data():
    return {"message": "Data from FastAPI"}

@app.post('/uploadfile/')
async def create_upload_file(file_uploads: list[UploadFile]):

    validate_columns(file_uploads)
    return {"filenames": [f.filename for f in file_uploads]}
    


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)