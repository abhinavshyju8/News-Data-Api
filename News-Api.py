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

for article in articles:
    title = article.get("title")
    source_name = article.get("source", {}).get("name")
    published_at = article.get("publishedAt")

    news_date = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ").date()

    sentiment_score = TextBlob(title).sentiment.polarity

    if sentiment_score > 0:
        sentiment_label = "Positive"
    elif sentiment_score < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    cur.execute("""
        INSERT INTO news_data
        (news_date, source_name, title, sentiment_score, sentiment_label)
        VALUES (%s, %s, %s, %s, %s)
    """, (news_date, source_name, title, sentiment_score, sentiment_label))

conn.commit()

print(f"{len(articles)} news articles inserted successfully!")
