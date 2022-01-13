from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Base
from database import engine
from routes import test

app = FastAPI()

app.include_router(test.router)

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(engine)
