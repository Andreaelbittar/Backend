from pydantic import BaseModel, Field
from typing import Optional

class genres(BaseModel):
    gen_id:Optional[int]=None
    gen_title: str= Field (max_length=20,min_length=3)

class Config:
    shema_extra={
        'example':{ 
            'gen_id':2,
            'gen_title': 'nametitle',
        }
    }