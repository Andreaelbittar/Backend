from msilib.schema import SelfReg
from typing import Self
from models.movie_genres import movie_genres as moviegenresModel

class moviegenresservice():
    def __init__ (self,db) -> None:
        self.db = db

    def get_movie_genres (self) -> moviegenresModel:
        result = self.db.query(moviegenresModel).all()
        return result
    
    def create_movie_genres(self, movie_genres:moviegenresModel):
        new_moviegenres = moviegenresModel(
            mov_id=movie_genres.mov_id,
            gen_id=movie_genres.gen_id
        ) 
        self.db.add(new_moviegenres)
        self.db.commit
        return