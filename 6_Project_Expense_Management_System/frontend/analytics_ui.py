import streamlit as st
from datetime import datetime
import requests
import pandas as pd



API_URL = "http://localhost:8000"


def analytics_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Select Start Date", datetime(2024, 8, 1))

    with col2:
        end_date = st.date_input("Select Start Date", datetime(2024, 8, 31))


    if st.button("Get Analytics"):
        payload={
            'start_date': start_date.strftime("%Y-%m-%d"),
            'end_date': end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics/",json=payload)
        if response.status_code==200:
            data=response.json()
            #st.write(data)


            table_data={
                "Category": list(data.keys()),
                "Total": [data[category]['Total']for category in data],
                "Percentage": [data[category]['Percentage']for category in data]
            }

            df= pd.DataFrame(table_data)

            df_sorted= df.sort_values(by="Percentage",ascending=False,ignore_index=True)
            total_sum = df_sorted["Total"].sum()

            st.bar_chart(data=df_sorted.set_index("Category")["Percentage"], width=0, height=0,
                         use_container_width=True)
            df_sorted["Total"]=df_sorted["Total"].map("{:.2f}".format)
            df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

            st.dataframe(df_sorted, use_container_width=True)

            #st.table(df_sorted)
            col3, col4, col5 = st.columns(3)
            with col5:
                st.text(f"Your Total Expense: {total_sum}")

