from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from schemas.movie_genres import movie_genres
from config.database import Session
from service.movie_genres import moviegenresservice

moviegenres_router = APIRouter()

@moviegenres_router.get('/movie_genres',tags=['movie_genres'],response_model=movie_genres,status_code= 200)
def get_moviegenres() -> movie_genres:
    db = Session ()
    result = moviegenresservice(db).get_moviegenres()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

    