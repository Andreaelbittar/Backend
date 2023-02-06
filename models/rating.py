from sqlalchemy import Column, ForeignKey ,Integer
from sqlalchemy.orm import relationship

class rating:

    __tablename__ = "rating"
mov_id= Column (Integer, ForeignKey('movie.id'))
rev_star= Column(Integer)
num_o_ratings= Column (Integer)
rev_id= Column (Integer,ForeignKey('reviewer.rev_id'))