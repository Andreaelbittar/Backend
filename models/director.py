from sqlalchemy import Column, ForeignKey ,Integer, String
from sqlalchemy.orm import relationship

class director:
     __tablename__ = "director"
     dir_id= Column(Integer, primary_key = True)
     dir_fname= Column (String)
     dir_lname= Column (String)
     