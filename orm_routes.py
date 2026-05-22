from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from models_db import (
    get_db,
    ExpenseDB,
    CategoryDB
)

from models import (
    Expense,
    ExpenseResponse,
    Category
)

router = APIRouter()

#add expesnses 
@router.post("/orm-add-expense")
def orm_add_expense(
    expense: Expense,
    db: Session = Depends(get_db)
):

    new_expense = ExpenseDB(
        title=expense.title,
        amount=expense.amount,
        category_id=expense.category_id
    )

    db.add(new_expense)

    db.commit()

    return {
        "message": "Expense added using ORM"
    }

#vies Expenses 
@router.get(
    "/orm-expenses",
    response_model=list[ExpenseResponse]
)
def orm_get_expenses(
    db: Session = Depends(get_db)
):

    expenses = db.query(ExpenseDB).all()

    results = []

    for expense in expenses:

        results.append({
            "id": expense.id,
            "title": expense.title,
            "amount": expense.amount,
            "category": expense.category.name
        })
    return results


#add catogary
@router.post("/orm-add-category")
def orm_add_category(
    category: Category,
    db: Session = Depends(get_db)
):

    new_category = CategoryDB(
        name=category.name
    )

    db.add(new_category)

    db.commit()

    return {
        "message": "Category added successfully"
    }

#get catogary
@router.get("/orm-categories")
def orm_get_categories(
    db: Session = Depends(get_db)
):

    categories = db.query(CategoryDB).all()

    results = []

    for category in categories:

        results.append({
            "id": category.id,
            "name": category.name
        })

    return results

#delete expenses 
@router.delete("/orm-delete-expense/{expense_id}")
def orm_delete_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):

    expense = db.query(ExpenseDB).filter(
        ExpenseDB.id == expense_id
    ).first()

    if not expense:

        return {
            "message": "Expense not found"
        }

    db.delete(expense)

    db.commit()

    return {
        "message": f"Expense {expense_id} deleted successfully"
    }

#update expeses 
@router.put("/orm-update-expense/{expense_id}")
def orm_update_expense(
    expense_id: int,
    expense: Expense,
    db: Session = Depends(get_db)
):

    existing_expense = db.query(ExpenseDB).filter(
        ExpenseDB.id == expense_id
    ).first()

    if not existing_expense:

        return {
            "message": "Expense not found"
        }

    existing_expense.title = expense.title
    existing_expense.amount = expense.amount
    existing_expense.category_id = expense.category_id

    db.commit()

    return {
        "message": f"Expense {expense_id} updated successfully"
    }

#update category
@router.put("/orm-update-category/{category_id}")
def orm_update_category(
    category_id: int,
    category: Category,
    db: Session = Depends(get_db)
):

    existing_category = db.query(CategoryDB).filter(
        CategoryDB.id == category_id
    ).first()

    if not existing_category:

        return {
            "message": "Category not found"
        }

    existing_category.name = category.name

    db.commit()

    return {
        "message": f"Category {category_id} updated successfully"
    }

#delete category
@router.delete("/orm-delete-category/{category_id}")
def orm_delete_category(
    category_id: int,
    db: Session = Depends(get_db)
):

    category = db.query(CategoryDB).filter(
        CategoryDB.id == category_id
    ).first()

    if not category:

        return {
            "message": "Category not found"
        }

    db.delete(category)

    db.commit()

    return {
        "message": f"Category {category_id} deleted successfully"
    }