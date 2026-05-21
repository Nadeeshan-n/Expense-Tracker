from pydantic import BaseModel


class Expense(BaseModel):

    
    title: str
    amount: float

class Catogary(BaseModel):
    name:str