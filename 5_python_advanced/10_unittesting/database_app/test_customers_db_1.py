import pytest
from customers_db import CustomersDB

def test_insert_customer():
    db=CustomersDB()
    db.connect()
    db.insert_customer('Virat Kohli','xyz@gmail.com')
    customer=db.get_customer_by_name('Virat Kohli')
    assert customer['name'] == "Virat Kohli"
    assert customer['email'] == "xyz@gmail.com"

    db.close()
def test_get_all_customer():
    db=CustomersDB()
    db.connect()
    db.insert_customer('Virat Kohli','xyz@gmail.com')
    db.insert_customer("Taylor Swift", "taylor@xyz.com")

    customers=db.get_all_customer()
    assert len(customers)==2

    db.close()