from models_db import (
    SessionLocal,
    ExpenseDB,
    CategoryDB
)

def create_expense_orm(
    title,
    amount,
    category_id
):

    db = SessionLocal()

    new_expense = ExpenseDB(
        title=title,
        amount=amount,
        category_id=category_id
    )

    db.add(new_expense)

    db.commit()

    db.close()


def get_expenses_orm():

    db = SessionLocal()

    expenses = (
        db.query(ExpenseDB)
        .join(CategoryDB)
        .all()
    )

    # Force relationship loading
    for expense in expenses:
        expense.category.name

    db.close()

    return expenses