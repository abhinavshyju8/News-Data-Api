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