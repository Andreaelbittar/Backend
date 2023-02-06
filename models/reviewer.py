from sqlalchemy import Column, ForeignKey ,Integer, CHAR
from sqlalchemy.orm import relationship

class reviewer:

    __tablename__ = "rewiever"
rev_id=Column(Integer,primary_key= True)
rev_name= Column (CHAR)