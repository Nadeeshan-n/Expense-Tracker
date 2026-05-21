from database import get_db_connection
from models import Expense, Catogary

#create the dtata base and insert ino expense table
def create_expense(title, amount):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (title, amount) VALUES (?, ?)",
        (title, amount)
    )

    conn.commit()
    conn.close()

#print all expenses
def get_all_expenses():

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    conn.close()

    return expenses

#delete a row by id
def delete_expense_by_id(expense_id):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()
    conn.close()


# update a raw by id 
def update_expense_by_id(expense_id, title, amount):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE expenses
        SET title = ?, amount = ?
        WHERE id = ?
        """,
        (title, amount, expense_id)
    )

    conn.commit()
    conn.close()

#add catogaries 
def create_category(name):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO categories (name) VALUES (?)",
        (name,)
    )

    conn.commit()
    conn.close()


def get_all_categories():

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM categories")

    categories = cursor.fetchall()

    conn.close()

    return categories