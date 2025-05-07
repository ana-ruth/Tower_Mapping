from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"ping": "pong"}

@app.get("/api/data")
def get_data():
    return {"message": "Data from FastAPI"}

@app.post('/uploadfile/')
async def create_upload_file(file_uploads: list[UploadFile]):
    for file_upload in file_uploads:
        data = await file_upload.read()
        print(f"Received file: {file_upload.filename}, Size: {len(data)} bytes")  # Log file name and size
        
    return {"filenames": [f.filename for f in file_uploads]}
    


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)