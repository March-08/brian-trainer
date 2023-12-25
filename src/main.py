from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from src.model.chain import chain

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://brian-frontend.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryBody(BaseModel):
    query: str

@app.post("/api/v0/query")
def query(body: QueryBody):
    return chain.predict_and_parse(text=body.query)["data"]["brian"][0]
