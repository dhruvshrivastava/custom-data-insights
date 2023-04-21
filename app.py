import streamlit as st

from multiapp import MultiApp
from apps import eda
from apps import models

st.set_page_config("Data Insights - PBL-III Project")

app = MultiApp()

app.add_app("Data Insights", eda.app)

app.run()
