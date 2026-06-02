import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(
    page_title="News Analytics Dashboard",
    layout="wide"
)

DATABASE_URL = "postgresql://postgres:News1234@news-db.ctkci2uuklt0.ap-south-2.rds.amazonaws.com:5432/postgres"

engine = create_engine(DATABASE_URL)