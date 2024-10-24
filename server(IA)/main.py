from typing import Union
from fastapi import FastAPI
from mqtt import mover_carrito
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/mover-carrito/")
def mover():
    mover_carrito()
    return {"logre enviar carrito"}