from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from schemas.movie_direction import movie_direction
from config.database import Session
from service.movie_direction import movie_directionservice

moviedirection_router = APIRouter()

@moviedirection_router.get ('/movie_direction', tags=['movie_direction'],response_model=movie_direction, status_code=200)
def get_moviedirection () -> movie_direction :
    db = Session ()
    result = movie_directionservice(db).get_moviedirection ()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)