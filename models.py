from pydantic import BaseModel


class Expense(BaseModel):

    title: str
    amount: float
    category_id: int


class ExpenseResponse(BaseModel):

    id: int
    title: str
    amount: float
    category: str


class Category(BaseModel):

    name: str

class UserCreate(BaseModel):

    username: str
    email: str
    password: str

class UserLogin(BaseModel):

    username: str
    password: str