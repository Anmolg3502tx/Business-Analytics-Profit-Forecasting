# Proprietary software developed for Radhe Krishn Enterprises.
# Business analytics logic is confidential and intended for internal use only.

import pandas as pd
import sqlite3
from config import DATABASE_PATH, CURRENCY, LOW_STOCK_THRESHOLD, DEAD_STOCK_DAYS

def get_sales_data():
    conn = sqlite3.connect(DATABASE_PATH)
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    return df

def get_inventory_data():
    conn = sqlite3.connect(DATABASE_PATH)
    df = pd.read_sql_query("SELECT * FROM inventory", conn)
    conn.close()
    return df

def get_expense_data():
    conn = sqlite3.connect(DATABASE_PATH)
    df = pd.read_sql_query("SELECT * FROM expenses", conn)
    conn.close()
    return df

def monthly_sales_summary(df):
    df['date'] = pd.to_datetime(df['date'])
    summary = df.groupby(df['date'].dt.to_period('M'))['total_amount'].sum()
    return summary

def yearly_sales_summary(df):
    df['date'] = pd.to_datetime(df['date'])
    summary = df.groupby(df['date'].dt.year)['total_amount'].sum()
    return summary

def top_selling_products(df, top_n=10):
    top = df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(top_n)
    return top

def slow_moving_products(df, threshold=5):
    slow = df.groupby('product_name')['quantity'].sum()
    slow = slow[slow <= threshold]
    return slow

def profit_loss_analysis(sales_df, expense_df):
    total_sales = sales_df['total_amount'].sum()
    total_expenses = expense_df['amount'].sum()
    profit = total_sales - total_expenses
    return {
        "total_sales": total_sales,
        "total_expenses": total_expenses,
        "profit": profit,
        "currency": CURRENCY
    }

def low_stock_alert(inventory_df):
    low = inventory_df[inventory_df['stock_quantity'] <= LOW_STOCK_THRESHOLD]
    return low

def dead_stock_detection(inventory_df):
    dead = inventory_df[inventory_df['days_in_stock'] >= DEAD_STOCK_DAYS]
    return dead

def pending_payments(invoice_df):
    conn = sqlite3.connect(DATABASE_PATH)
    invoice_df = pd.read_sql_query("SELECT * FROM invoices", conn)
    conn.close()
    pending = invoice_df[invoice_df['payment_status'] == 'Pending']
    return pending

def cash_flow_analysis(sales_df, expense_df):
    sales_df['date'] = pd.to_datetime(sales_df['date'])
    expense_df['date'] = pd.to_datetime(expense_df['date'])
    monthly_income = sales_df.groupby(sales_df['date'].dt.to_period('M'))['total_amount'].sum()
    monthly_expense = expense_df.groupby(expense_df['date'].dt.to_period('M'))['amount'].sum()
    cash_flow = monthly_income - monthly_expense
    return cash_flow
