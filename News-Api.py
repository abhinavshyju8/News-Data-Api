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

url = "https://newsapi.org/v2/top-headlines"

params = {
    "q": "AI",
    "language": "en",
    "pageSize": 40,
    "apiKey": API_KEY
}

response = requests.get(url, params=params)
articles = response.json().get("articles", [])

cur = conn.cursor()
