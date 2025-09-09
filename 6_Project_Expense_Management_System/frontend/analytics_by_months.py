import streamlit as st
import datetime
from datetime import date
import requests
import pandas as pd



API_URL = "http://localhost:8000"

def analytics_by_months():
    today= date.today()
    past_six_months= today - datetime.timedelta(days=6*30)
    col1, col2 = st.columns(2)
    with col1:
        past_date = st.date_input("Select past months date", past_six_months)
    with col2:
        current_date=st.date_input("Select current date",today,max_value=today)

    if st.button("Get Analysis"):
        payload={
            "start_date":past_date.strftime("%Y-%m-%d"),
            "end_date":current_date.strftime("%Y-%m-%d")
        }

        response= requests.post(f"{API_URL}/monthly_summary",json=payload)
        if response.status_code==200:
            data=response.json()

            table_data={
                "Months":[row['month']for row in data],
                "Total": [row['total']for row in data]
            }
            df=pd.DataFrame(table_data)
            df_sorted = df.sort_values(by="Total", ascending=False, ignore_index=True)

            st.bar_chart(data=df_sorted.set_index("Months")["Total"], width=0, height=0,
                         use_container_width=True)

            st.dataframe(df_sorted, use_container_width=True)
