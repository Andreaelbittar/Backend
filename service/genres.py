from models.genres import genres as genresmodel

class GenresService():
    def __init__(self,db) -> None:
        self.db = db
    
    def get_gneres (self) -> genresmodel:
        result = self.db.query(genresmodel).all()
        return result
    
    def creater_gneres (self, gnres:genresmodel):
        new_gnres = gneresmodel(
            gen_id = genres.gen_id,
            gen_title = genres.gen_title
        )
        self.db.add(new_gnres)
        self.db.coomit()
        return
