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
st.sidebar.markdown("""
<div class="sidebar-text">
Sentiment score indicates whether the news sentiment is positive or negative.

Scores above 0 are positive.  
Scores below 0 are negative.  
Scores near 0 are neutral.
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### Latest update data")
if not df.empty:
    st.sidebar.write(df["created_at"].max())

st.markdown('<div class="main-title">News analytics sentiment score dashboard</div>', unsafe_allow_html=True)

if df.empty:
    st.warning("No news data found in database.")
else:
    display_df = df[
        [
            "news_date",
            "source_name",
            "title",
            "sentiment_score",
            "sentiment_label",
            "created_at"
        ]
    ]

    def color_sentiment(value):
        if value > 0:
            return "background-color: green; color: white"
        elif value < 0:
            return "background-color: red; color: white"
        else:
            return "background-color: gray; color: white"
        
    styled_df = display_df.style.map(
        color_sentiment,
        subset=["sentiment_score"]
    )
