from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, formdata

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(formdata.router)
@app.get("/")
def read_root():
    return {"message": "API is running. See /docs for Swagger UI."}