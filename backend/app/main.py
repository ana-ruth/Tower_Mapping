from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


@app.get("/")
async def root():
    return {"ping": "pong"}

@app.get("/api/data")
def get_data():
    return {"message": "Data from FastAPI"}

    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)