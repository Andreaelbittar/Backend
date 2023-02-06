from sqlalchemy import ForeignKey, Column, Integer
from sqlalchemy.orm import relationship

from config.database import Base

class movie_genres:
    __tablename_= 'movie_genres'
    mov_id= Column(Integer,ForeignKey('movie.id'))
    gen_id= Column(Integer,ForeignKey('genres.gen_id'))