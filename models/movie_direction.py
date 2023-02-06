from sqlalchemy import Column, ForeignKey ,Integer
from sqlalchemy.orm import relationship

class Movie_direction:

    __tablename__ = "movie_direction"
mov_id= Column (Integer, ForeignKey('movie.id'))
dir_id= Column (Integer, ForeignKey('director.dir_id'))
