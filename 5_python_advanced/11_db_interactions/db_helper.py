import mysql.connector
from contextlib import contextmanager

@contextmanager
def get_gb_connection_cursor(commit=False):

    connection= mysql.connector.connect(
        host='localhost',
        user='root',
        password='9871003320@Ch',
        database="expense_manager"
    )

#    if connection.is_connected():
#        print("")
#    else:
#        print("Connection failed ")
    cursor=connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()

    cursor.close()
    connection.close()


def fetch_all_records():
    with get_gb_connection_cursor() as cursor:

        cursor.execute('SELECT * FROM expense_manager.expenses;')
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

def fetch_expenses_for_date(expense_date):
    with get_gb_connection_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date=%s", (expense_date,))
        expenses=cursor.fetchall()
        for expense in expenses:
            print(expense)



def insert_expense(expense_date,amount,category,notes):
    with get_gb_connection_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s,%s,%s,%s)",
                       (expense_date, amount,category, notes)
                       )

def delete_expenses_for_date(expense_date):
    with get_gb_connection_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s",(expense_date,))


if __name__=="__main__":
    #fetch_expenses_for_date("2024-08-20")
    print("All expenses".center(50,"*"))
    fetch_all_records()
    print("Fetch expenses for date  after insert ".center(100, "*"))
    insert_expense("2024-08-20", 300, "Food", "Panipuri")
    fetch_expenses_for_date("2024-08-20")
    print("Fetch expenses for date  after delete for that date ".center(100, "*"))
    delete_expenses_for_date("2024-08-20")
    fetch_expenses_for_date("2024-08-20")
#

