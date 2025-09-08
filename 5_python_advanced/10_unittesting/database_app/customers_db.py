class CustomersDB:
    def __init__(self):
        self.customers=[]
        self.next_id=1
        self.connection=None

    def connect(self):
        self.connection="DummyConnectObject"
        print("Connected to Database")

    def insert_customer(self,name,email):

        customer={

            'id': self.next_id,
            'name':name,
            'email':email

        }
        self.customers.append(customer)
        self.next_id+=1

    def get_all_customer(self):
        return self.customers

    def get_customer_by_name(self,name):
        for customer in self.customers:
            if customer['name']==name:
                return customer
        return None
    def clear_customer(self):
        self.customers=[]
        self.next_id=1

    def close(self):
        self.connection=None
        print("Database connection closed")



if __name__=="__main__":
    db=CustomersDB()
    db.connect()
    db.insert_customer('Harsh Chauhan','hc063213@gmail.com')
    print(db.get_all_customer())
    print(db.get_customer_by_name("Harsh Chauhan"))
    db.clear_customer()
    db.close()