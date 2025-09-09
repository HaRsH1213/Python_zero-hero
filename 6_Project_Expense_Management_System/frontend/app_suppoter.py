import streamlit as st
import requests

class FormHandler:
    def __init__(self, API_URL = "http://localhost:8000", category = ["Food","Rent","Shopping","Entertainment","Other"],selected_date=None):
        self.category=category
        self.API_URL=API_URL
        self.selected_date=selected_date



    def existing_expenses_form(self,existing_expenses):
        expenses=[]
        if st.button("Get Expenses"):
            st.session_state["show_expenses_form"] = True

        if st.session_state.get("show_expenses_form"):
            with st.form(key="expense_form"):
                col_1, col_2, col_3 = st.columns(3)
                with col_1:
                    st.subheader("Amount")
                with col_2:
                    st.subheader("Category")

                with col_3:
                    st.subheader("Notes")

                for i in range(len(existing_expenses)):
                    amount = existing_expenses[i]["amount"]
                    category = existing_expenses[i]["category"]
                    notes = existing_expenses[i]['notes']

                    with col_1:
                        amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}", label_visibility="collapsed")

                    with col_2:
                        category_input = st.selectbox(label="Category", options=self.category, index=self.category.index(category),key=f"category_{i}", label_visibility="collapsed", )

                    with col_3:
                        notes_input=st.text_input(label="Notes", value=notes, key=f"notes_{i}", label_visibility="collapsed")

                    expenses.append({
                        'amount': amount_input,
                        'category': category_input,
                        'notes': notes_input
                    })

                update_button = st.form_submit_button("Update")
                if update_button:
                    response=requests.post(f"{self.API_URL}/expenses/{self.selected_date}",json=expenses)
                    if response.status_code==200:
                        st.success("Expenses Update Successfully!")

                    else:
                        st.error("Failed to update expenses")

                    st.session_state["show_expenses_form"] = False


    def add_new_expenses(self):
        expenses=[]
        if st.button("Add Expenses"):
            st.session_state["adding_expenses"] = True

            # Step 2: Show form if state is active
        if st.session_state.get("adding_expenses"):
            number_of_expenses = st.number_input(label="Total number of expenses",min_value=1,step=1,value=5,)
            with st.form(key="add_new_expense_form"):
                col_1, col_2, col_3 = st.columns(3)
                with col_1:
                    st.subheader("Amount")
                with col_2:
                    st.subheader("Category")

                with col_3:
                    st.subheader("Notes")

                for i in range(number_of_expenses):
                    with col_1:
                        amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, key=f"new_amount_{i}", placeholder = "Enter your expense amount", label_visibility="collapsed")

                    with col_2:
                        category_input = st.selectbox(label="Category",placeholder = "Select Category", options=self.category,key=f"new_category_{i}", label_visibility="collapsed", )

                    with col_3:
                        notes_input = st.text_input(label="Notes",key=f"new_notes_{i}",placeholder = "Write a note", label_visibility="collapsed")

                    expenses.append({
                        'amount': amount_input,
                        'category': category_input,
                        'notes': notes_input
                    })

                add_button = st.form_submit_button("Add")
                if add_button:
                    response = requests.post(f"{self.API_URL}/expenses/{self.selected_date}", json=expenses)
                    if response.status_code == 200:
                        st.success("Expenses Add Successfully!")

                    else:
                        st.error("Failed to add expenses")
                    st.session_state["adding_expenses"] = False




