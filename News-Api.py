import os
import requests
import psycopg2
from textblob import TextBlob
from datetime import datetime

API_KEY = os.getenv("NEWS_API_KEY")

conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)
