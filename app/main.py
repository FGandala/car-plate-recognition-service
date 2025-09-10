from fastapi import FastAPI
from app.api.endpoints import recognize

app = FastAPI(title="Carplate recognition service")

app.include_router(
    recognize.router,
    prefix='/api/v1',
    tags=['Video Streaming']
)

@app.get("/")
def read_root():
  return {"message":"Bem vindo à API"}