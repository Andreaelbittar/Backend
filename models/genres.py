from sqlalchemy import ForeignKey, Column, CHAR, Integer 
from sqlalchemy.orm import relationship

from config.database import Base

class genres:
    __tablename__='genres'
gen_id= Column(Integer,primary_key= True)
gen_title= Column(CHAR)
