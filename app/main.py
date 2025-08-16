<<<<<<< Updated upstream
from fastapi import FastAPI

app = FastAPI(title="Carplate recognition service")

@app.get("/")
def read_root():
=======
from fastapi import FastAPI
from app.api.endpoints import streaming

app = FastAPI(title="Carplate recognition service")

app.include_router(
    streaming.router,
    prefix='/api/v1',
    tags=['Video Streaming']
)

@app.get("/")
def read_root():
>>>>>>> Stashed changes
    return {"message":"Bem vindo à API"}