from msilib.schema import SelfReg
from typing import Self
from models.reviewer import reviewer as reviewerModel

class reviewerservice ():

    def __init__(self,db) -> None:
        self.db = db
    
    def get_reviewer (self) ->reviewerModel:
        result = self.db.query(reviewerModel).all()
        return result

    def create_reviewer(self,reviewer: reviewerModel):
        new_reviewer= DirectorModel(
            rev_id = reviewer.rev_id,
            rev_name = reviewer.rev_name,
        )
        self.db.add(new_reviewer)
        self.db.commit
        return