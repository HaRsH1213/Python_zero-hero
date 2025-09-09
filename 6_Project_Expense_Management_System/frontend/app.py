import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab
from analytics_by_months import analytics_by_months



st.title("Expense Tracking System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics_by_category", "Analytics_by_months"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_by_months()