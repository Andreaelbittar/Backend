from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from schemas.director import director
from config.database import Session
from service.director import DirectorService

director_router = APIRouter()

@director_router.get('/director',tags=['director'], response_model=director,status_code= 200)
def get_director() -> director:
    db = Session ()
    result = DirectorService(db).get_director()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)
    