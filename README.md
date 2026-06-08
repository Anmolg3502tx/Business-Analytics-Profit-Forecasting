
# Business Analytics and Profit Forecasting System

A real-time AI-powered business analytics solution built for Radhe Krishn Enterprises, a ladies fancy wear footwear manufacturing and wholesale company. The system automates billing, invoicing, inventory management, profit forecasting, and provides an AI chatbot for instant business insights.

I built this during my internship at Radhe Krishn Enterprises. My uncle was manually tracking everything — sales, stock, expenses, retailer payments — in registers. There was no way to quickly know how the business was performing. I wanted to fix this with an automated system that gives instant answers.


## Why I Built This

Radhe Krishn Enterprises deals in manufacturing ladies fancy wear footwear and wholesaling branded footwear to retailers. Managing inventory, tracking retailer payments, calculating monthly profits, and generating invoices manually was time consuming and error prone. I built this system to automate all of it and give my uncle a clear picture of his business at any time.


## What It Does

Tracks sales, expenses, inventory, and profitability in real time. Generates automated invoices and billing. Provides an AI-powered chatbot that answers business questions like monthly profit, top selling products, pending payments, and future sales predictions. Everything is visible on a single dashboard.


## Features

**Sales and Revenue**
- Daily, weekly, monthly, and yearly sales tracking
- Top selling products ranking
- Slow moving products alert
- Season wise sales comparison
- Retailer wise sales tracking

**Inventory and Stock**
- Real-time inventory management
- Low stock alerts when items are running out
- Dead stock detection for items not sold in a long time
- Stock aging report
- Return and damage tracking

**Finance and Profit**
- Profit and loss analysis monthwise and yearwise
- Expense tracking and category wise breakup
- GST calculation automation
- Payment pending tracking for retailers
- Cash flow analysis
- Anomaly detection for unusual losses or expenses

**Billing and Invoicing**
- Automated invoice generation
- PDF report generation monthly
- Excel export of any data

**AI Chatbot**
- Ask questions like "How much profit did I make this month?"
- Monthly and yearly sales summary
- Future sales prediction for next month
- "Which product should I order more this season?"
- Automatic weekly summary report on Telegram
- Powered by Google Gemini API

**Dashboard**
- Single screen view of all business data
- Graphs and charts for sales, profit, inventory
- Dark mode support


## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core logic |
| Pandas | Data analysis |
| Plotly | Interactive graphs and charts |
| Streamlit | Dashboard and UI |
| OpenPyXL | Excel report generation |
| SQLite | Database |
| Google Gemini API | AI chatbot for business insights |


## How It Works

Sales, expenses, and inventory data is stored in a SQLite database. Pandas processes and analyses the data. Streamlit displays everything on a live dashboard with Plotly charts. When the shop owner asks a question in the chatbot, Gemini API reads the business data and gives an instant answer in plain language.


## Sample Output



![Demo](assets/demo.png)


*Monthly profit analysis dashboard with AI chatbot*


## Run It

```bash
git clone https://github.com/Anmolg3502tx/Business-Analytics-Profit-Forecasting
cd Business-Analytics-Profit-Forecasting
pip install -r requirements.txt
streamlit run app.py
```

## Future Improvements

The next version will include WhatsApp integration for automated weekly business reports, multi-branch support for businesses with more than one location, and a mobile app version for on-the-go access.


## Built By

Anmol Gupta, B.Tech CSE (AI & ML), KR Mangalam University.
Built during internship at Radhe Krishn Enterprises, Haryana.
```

---
