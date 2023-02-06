from msilib.schema import SelfReg
from typing import Self
from models.movie_direction import Movie_direction as movie_directionMoldel

class movie_directionservice(): 

    def __init__(self,db) -> None:
        self.db = db
    
    def get_movie_direction (self) -> movie_directionMoldel:
        result = self.db.query(movie_directionMoldel).all()
        return result

    def movie_direction  (self,movie_direction : movie_directionMoldel):
        new_movie_direction = movie_directionMoldel(
            mov_id = movie_direction.mov_id,
            dir_id = movie_direction.dir_id,
        )
        self.db.add(new_movie_direction)
        self.db.commit
        return
    