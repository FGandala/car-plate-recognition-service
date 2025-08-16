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
    return {"message":"Bem vindo à API"}