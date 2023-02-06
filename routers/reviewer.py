from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from schemas.reviewer import reviewer
from config.database import Session
from service.reviewer import reviewerservice

reviewer_router = APIRouter()

@reviewer_router.get('/reviewer',tags=['reviewer'], response_model=reviewer,status_code= 200)
def get_reviewer() -> reviewer:
    db = Session ()
    result = reviewerservice(db).get_reviewer()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)
    