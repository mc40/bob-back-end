from typing import Optional
from fastapi import FastAPI, HTTPException
import json
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/tpd/{combo_id}")
def tpd(combo_id: float):
    f = open('data.json')
    data = json.load(f)
    result = None
    for idx, ele in enumerate(data):
        if (float(ele['Power Demand']) - combo_id >= 0):
            print(float(ele['Power Demand']) - combo_id)
            if result == None:
                result = idx
            elif (float(ele['Power Demand']) - combo_id) < float(data[result]['Power Demand']) - combo_id:
                result = idx
    if result == None:
        return "no data"
    return data[result]