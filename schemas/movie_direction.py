from typing import Optional
from pydantic import BaseModel, Field

class movie_direction(BaseModel):
    mov_id= int
    dir_id =int

class config:
        schema_extra= {
             'example':{
                'mov_id':'1',
                'dir_id':'1',
             }

        }
