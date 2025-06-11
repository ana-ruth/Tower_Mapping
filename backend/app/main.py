from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile

from .towerProcessor import *
from .reportGenerator import *

#from towerProcessor import *
#from reportGenerator import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://tower-mapping.vercel.app"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"ping": "pong"}

@app.get("/api/data")
def get_data():
    return {"message": "Data from FastAPI"}

@app.post('/uploadfile/')
async def create_upload_file(file_uploads: list[UploadFile]):

    try:
        df = validate_columns(file_uploads)
        report = generate_report(df)
        return {"filenames": [f.filename for f in file_uploads]}
    except Exception as e:
        raise HTTPException(status_code = 400, detail =str(e))
    


