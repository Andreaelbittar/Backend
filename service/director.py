from msilib.schema import SelfReg
from typing import Self
from models.director import director as DirectorModel

class DirectorService(): 

    def __init__(self,db) -> None:
        self.db = db
    
    def get_director (self) -> DirectorModel:
        result = self.db.query(DirectorModel).all()
        return result

    def create_director (self,director: DirectorModel):
        new_director = DirectorModel(
            dir_id = director.dir_id,
            dir_fname = director.dir_fname,
            dir_lname = director.dir_lname
        )
        self.db.add(new_director)
        self.db.commit
        return