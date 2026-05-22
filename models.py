from pydantic import BaseModel


class Expense(BaseModel):

    
    title: str
    amount: float
    Category_id: int

class Catogary(BaseModel):
    name:str