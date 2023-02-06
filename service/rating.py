from msilib.schema import SelfReg
from typing import Self
from models.rating import rating as ratingModel

class ratingservice(): 

    def __init__(self,db) -> None:
        self.db = db
    
    def get_rating(self) -> ratingModel:
        result = self.db.query(ratingModel).all()
        return result

    def create_rating (self,director: ratingModel):
        new_rating = ratingModel(
            mov_id = rating.mov_id,
            rev_star = rating.rev_star,
            num_o_ratings = rating.num_o_ratings,
            rev_id = rating.rev_id
        )   
        self.db.add(new_director)
        self.db.commit
        return