from fastapi import FastAPI

app = FastAPI(title="Carplate recognition service")

@app.get("/")
def read_root():
    return {"message":"Bem vindo à API"}