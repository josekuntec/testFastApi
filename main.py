from fastapi import FastAPI, Form
from typing import Annotated
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class FormData(BaseModel):
    primero: str
    segundo: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/suma")
def suma(item: Annotated[FormData, Form()]):
    x = int(item.primero)
    y = int(item.segundo)
    resultado = x+y
    return str(resultado)
