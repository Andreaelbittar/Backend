from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from schemas.rating import rating
from config.database import Session
from service.rating import ratingservice

rating_router = APIRouter()

@rating_router.get('/rating',tags=['rating'], response_model=rating,status_code= 200)
def get_rating() -> rating:
    db = Session ()
    result = ratingservice(db).get_rating()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)
    