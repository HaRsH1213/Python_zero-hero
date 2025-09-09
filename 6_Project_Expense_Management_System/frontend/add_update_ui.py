import streamlit as st
from datetime import datetime
import requests
from app_suppoter import FormHandler

API_URL = "http://localhost:8000"

def add_update_tab():
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