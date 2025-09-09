import streamlit as st
from datetime import datetime
import requests
from app_suppoter import FormHandler


API_URL = "http://localhost:8000"

st.title("Expense Tracking System")

tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    selected_date = st.date_input("Enter date",datetime(2024,8,1))
    response=requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code==200:
        existing_expenses=response.json()
        if len(existing_expenses)>0:
            form=FormHandler(selected_date=selected_date)
            form.existing_expenses_form(existing_expenses)
        #st.write(existing_expenses)
        else:
            form = FormHandler(selected_date=selected_date)
            form.add_new_expenses()


    else:
        st.error("Failed to retrieve expenses")
        existing_expenses=[]



with tab2:
    stat_date = st.date_input("Select Start Date",datetime(2024,8,1))
    end_date = st.date_input("Select Start Date",datetime(2024,8,31))
    response=requests.post(f"{API_URL}/analytics/")
    st.s