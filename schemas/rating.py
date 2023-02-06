from pydantic import BaseModel, Field


class rating (BaseModel):
    mov_id:int
    rev_star: int
    num_o_ratings: int
    rev_id:int

class Config:
    shema_extra={
        'example':{ 
            'mov_id:': '1',
            'rev_star': '4',
            'num_o_ratings': '2',
            'rev_id':'3'
        }
    }