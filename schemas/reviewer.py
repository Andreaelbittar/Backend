from pydantic import BaseModel, Field


class reviewer (BaseModel):
    rev_id:int
    rev_name: str = Field(max_length=15, min_length=3)

class Config:
    shema_extra={
        'example':{ 
            'rev_id:': '1',
            'rev_name': '4',
     
        }
    }