import pytest
from customers_db import CustomersDB

@pytest.fixture
def db():
    db_instance=CustomersDB()
    db_instance.connect()
    yield db_instance
    db_instance.close()

def test_insert_customers(db):
    db.insert_customer('Virat Kohli','xyz@gamil.com')
    customer=db.get_customer_by_name('Virat Kohli')
    assert customer is not None
    assert customer['name']=='Virat Kohli'
    assert customer['email']=='xyz@gamil.com'

def test_get_all_customers(db):
    db.insert_customer('Virat Kohli', 'xyz@gmail.com')
    db.insert_customer("Taylor Swift", "taylor@xyz.com")

    customers=db.get_all_customer()
    assert len(customers)==2

