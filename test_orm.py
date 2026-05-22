from orm_crud import get_expenses_orm

expenses = get_expenses_orm()

for expense in expenses:

    print("Title:", expense.title)

    print("Amount:", expense.amount)

    print("Category:", expense.category.name)

    print("-------------------")