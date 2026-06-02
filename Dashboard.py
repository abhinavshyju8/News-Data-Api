import streamlit as st
import pandas as pd
import os
from sqlalchemy import create_engine

st.set_page_config(
    page_title="News Analytics Dashboard",
    layout="wide"
)

DATABASE_URL =os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

df = pd.read_sql("SELECT * FROM news_data ORDER BY created_at DESC", engine)

st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main-title {
    font-size: 42px;
    font-weight: bold;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}
.sidebar-text {
    font-size: 15px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.radio(
    "Navigation",
    ["View News", "Analytics"]
)

st.sidebar.markdown("### Explanation")
