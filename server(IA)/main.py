from fastapi import FastAPI
from mqtt import mover_carrito

app = FastAPI()

@app.get("/")
def read_root():
    return {"hola": "mundo"}

@app.get("/mover-carrito/")
def mover():
    response = mover_carrito()
    return response