from fastapi import FastAPI
from models import Expense
from models import Catogary

#import crud (dtatabase handling)
from crud import (
    create_expense,
    get_all_categories,
    get_all_expenses,
    delete_expense_by_id,
    update_expense_by_id,
    create_category,
    
)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Expense Tracker Backend Running"
    }


@app.post("/add-expense")
def add_expense(expense: Expense):

    create_expense(
        expense.title,
        expense.amount,
        expense.Category_id
    )

    return {
        "message": "Expense added successfully"
    }


@app.get("/expenses")
def get_expenses():

    expenses = get_all_expenses()

    return {
        "expenses": expenses
    }


@app.delete("/delete-expense/{expense_id}")
def delete_expense(expense_id: int):

    delete_expense_by_id(expense_id)

    return {
        "message": f"Expense {expense_id} deleted successfully"
    }
@app.put("/update-expense/{expense_id}")
def update_expense(
    expense_id: int,
    expense: Expense
):

    update_expense_by_id(
        expense_id,
        expense.title,
        expense.amount
    )

    return {
        "message": f"Expense {expense_id} updated successfully"
    }

@app.post("/add-category")
def add_category(category: Catogary):

    create_category(
        category.name
    )

    return {
        "message": "Category added successfully"
    }

@app.get("/categories")
def get_categories():

    categories = get_all_categories()

    return {
        "categories": categories
    }
