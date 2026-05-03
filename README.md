# Price-intelligent-pipeline
Price monitoring pipeline

🛍️ Price Intelligence Pipeline (Consumer Behavior Tracking System)

📌 Overview

This project is a data engineering pipeline designed to track product prices over time and generate actionable insights such as optimal buying windows and price drop alerts.

It simulates real-world consumer behavior tracking by collecting, storing, and analyzing price data from e-commerce platforms like AJIO and Myntra.

---

🎯 Problem Statement

Consumers often face uncertainty about:

- When to purchase a product at the lowest price
- Whether a discount is genuine or inflated
- How prices fluctuate over time

This project solves that by building a historical price tracking and analysis system.

---

💡 Solution

The system:

1. Scrapes product price data periodically
2. Stores historical price records
3. Applies transformation logic to detect trends
4. Generates “Buy Signals” based on rolling minimum prices
5. Exposes insights via a REST API

---

🏗️ Architecture

Web Scraper (Python)
        ↓
Raw Data Storage (CSV)
        ↓
Data Transformation (Pandas)
        ↓
Business Logic (Price Analysis)
        ↓
FastAPI Service (REST API)
        ↓
User / Dashboard

---

⚙️ Tech Stack

- Python – Data ingestion & processing
- Pandas – Data transformation & analysis
- FastAPI – REST API layer
- BeautifulSoup – Web scraping
- Uvicorn – API server

(Future Enhancements: PostgreSQL, Apache Airflow, Docker)

---

🔄 Data Pipeline Flow

1. Ingestion Layer
   
   - Scrapes product price from web page
   - Stores timestamped records

2. Transformation Layer
   
   - Cleans price data (₹, commas removed)
   - Converts to numeric format

3. Analysis Layer
   
   - Computes rolling minimum price (14-day window)
   - Detects price drops
   - Generates Buy Signal

4. Serving Layer
   
   - REST API exposes processed insights

---

📡 API Endpoints

🔹 Get Recent Prices

GET /prices

🔹 Get Buy Signal

GET /buy-signal

Response Example:

{
  "current_price": 2499,
  "min_price": 2299,
  "buy": false
}

---

🧠 Key Features

- 📊 Historical price tracking
- 🔍 Price trend analysis
- 🚨 Buy signal detection
- ⚡ Lightweight REST API
- 🔄 Modular pipeline design

---

🚀 How to Run

1. Install Dependencies

pip install -r requirements.txt

2. Run Scraper

python scraper.py

3. Start API Server

uvicorn api:app --reload

4. Open API Docs

http://127.0.0.1:8000/docs

---

📈 Sample Use Case

A user tracks a product for 2 weeks.
The system identifies the lowest price point and triggers a:

«🔥 BUY SIGNAL when current price ≤ historical minimum»

---

🔮 Future Enhancements

- PostgreSQL integration (data warehouse layer)
- Apache Airflow for scheduling pipelines
- Multi-product tracking
- Cross-platform price comparison (AJIO vs Myntra)
- Notification system (Email/Telegram alerts)

---

🧭 Learnings & Outcomes

- Designed an end-to-end data pipeline
- Implemented ETL (Extract, Transform, Load) workflow
- Built REST APIs for data access
- Applied time-series analysis for decision-making

---

📌 Conclusion

This project demonstrates how data engineering principles can be applied to real-world consumer problems by transforming raw data into actionable insights.



