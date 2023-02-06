from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from schemas.genres import genres
from config.database import Session
from service.genres import GenresService

genres_router = APIRouter()

@genres_router.get('/genres',tags=['genres'],response_model=genres, status_code=200)
def get_genres() -> genres:
    db = Session ()
    result = GenresService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)
