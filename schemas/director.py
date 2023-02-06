from typing import Optional
from pydantic import BaseModel, Field

class director (BaseModel):
    dir_id:  Optional[int] = None
    dir_fname: str = Field (max_length=15,min_length=3)
    dir_lname: str = Field (max_length=25, min_length=3)

class Config:
    schema_extra = {
        "example":{
            'dir_id':1,
            'dir_fname':'Gillermo',
            'dir_lname': 'Toro',
        }
    }