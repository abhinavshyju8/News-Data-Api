News Sentiment Analysis Pipeline on AWS

A serverless and containerized data pipeline that collects news articles from an external News API, performs sentiment analysis, stores processed data in PostgreSQL (Amazon RDS), archives raw JSON files in Amazon S3, and visualizes insights through a Streamlit dashboard running on AWS ECS Fargate.

📌 Architecture Overview

Workflow
Amazon EventBridge triggers an AWS Lambda function every 5 minutes.
AWS Lambda:
Fetches news articles from a News API.
Performs sentiment analysis on article content.
Stores processed articles and sentiment scores in Amazon RDS (PostgreSQL).
Saves raw news responses as JSON files in Amazon S3.
Amazon RDS (PostgreSQL) serves as the primary database for structured news and sentiment data.
Amazon S3 stores raw article data for backup and future processing.
A Streamlit Dashboard is containerized using Docker.
The Docker image is pushed to Amazon ECR (Elastic Container Registry).
Amazon ECS Fargate deploys and runs the Streamlit application.
The dashboard queries PostgreSQL and displays analytics through a web interface.
🏗️ Architecture Components
Service	Purpose
Amazon EventBridge	Scheduled execution every 5 minutes
AWS Lambda	Data ingestion, sentiment analysis, storage
News API	Source of news articles
Amazon RDS PostgreSQL	Structured storage for processed articles
Amazon S3	Storage for raw JSON files
Amazon ECR	Docker image repository
Amazon ECS Fargate	Container hosting for Streamlit dashboard
Streamlit	Interactive analytics dashboard
🚀 Features
Automated news collection every 5 minutes
Sentiment analysis of news articles
PostgreSQL-based data storage
Raw data archival in S3
Containerized dashboard deployment
Serverless ingestion architecture
Scalable AWS-native solution
Near real-time visualization
📂 Project Structure
project-root/
│
├── lambda/
│   ├── lambda_function.py
│   ├── sentiment_analysis.py
│   └── requirements.txt
│
├── dashboard/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── infrastructure/
│   ├── terraform/
│   └── cloudformation/
│
├── data/
│   └── sample_news.json
│
├── Architecture.jpeg
│
└── README.md
🔄 Data Flow
EventBridge
     │
     ▼
 AWS Lambda
     │
 ┌───┴───────────────┐
 │                   │
 ▼                   ▼
Amazon RDS      Amazon S3
(PostgreSQL)    (Raw JSON)
 │
 ▼
Streamlit Dashboard
 │
 ▼
ECS Fargate
⚙️ Deployment Steps
1. Create AWS Resources
Amazon RDS PostgreSQL instance
Amazon S3 bucket
Amazon ECR repository
ECS Fargate Cluster
EventBridge Rule
IAM Roles and Policies
2. Deploy Lambda Function
zip lambda.zip lambda_function.py requirements.txt

aws lambda create-function \
  --function-name news-sentiment-processor \
  --runtime python3.11 \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://lambda.zip
3. Configure EventBridge Schedule
rate(5 minutes)
4. Build and Push Streamlit Docker Image
docker build -t news-dashboard .

aws ecr get-login-password \
| docker login --username AWS \
--password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com

docker tag news-dashboard:latest \
<account-id>.dkr.ecr.<region>.amazonaws.com/news-dashboard:latest

docker push \
<account-id>.dkr.ecr.<region>.amazonaws.com/news-dashboard:latest
5. Deploy to ECS Fargate

Create:

ECS Cluster
Task Definition
Service
Security Groups

Configure the task to pull the image from ECR.

📊 Dashboard

The Streamlit dashboard provides:

Latest news articles
Sentiment distribution
Positive vs Negative trends
Article count metrics
Historical sentiment analysis
Search and filtering capabilities

Default access:

http://<ecs-public-ip>:8051
🗄️ Database Schema Example
CREATE TABLE news_articles (
    id SERIAL PRIMARY KEY,
    title TEXT,
    source VARCHAR(255),
    published_at TIMESTAMP,
    sentiment VARCHAR(50),
    sentiment_score FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
🔒 Security Considerations
Store API keys in AWS Secrets Manager
Use IAM least-privilege permissions
Enable RDS encryption
Restrict ECS access through security groups
Enable S3 bucket encryption
Use HTTPS via Application Load Balancer
📈 Future Enhancements
Multi-source news aggregation
Advanced NLP models (BERT, FinBERT)
Real-time streaming with Amazon Kinesis
Alerting on sentiment spikes
Historical trend forecasting
CI/CD pipeline using GitHub Actions
🛠️ Tech Stack
Python
AWS Lambda
Amazon EventBridge
Amazon RDS PostgreSQL
Amazon S3
Docker
Amazon ECR
Amazon ECS Fargate
Streamlit
News API
Sentiment Analysis (NLTK / TextBlob / Transformers)
👤 Author
Abhinav Shyju C

A cloud-native news analytics platform built using AWS serverless services and containerized applications to provide automated sentiment-driven insights from real-time news data.
