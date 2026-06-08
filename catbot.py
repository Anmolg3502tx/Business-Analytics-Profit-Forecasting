# Proprietary software developed for Radhe Krishn Enterprises.
# AI chatbot logic and Gemini API integration is confidential.
# API keys and credentials have been removed for security purposes.

import google.generativeai as genai
from config import GEMINI_API_KEY
from analytics import (
    get_sales_data,
    get_expense_data,
    get_inventory_data,
    monthly_sales_summary,
    yearly_sales_summary,
    profit_loss_analysis,
    top_selling_products,
    low_stock_alert
)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def build_business_context():
    sales_df = get_sales_data()
    expense_df = get_expense_data()
    inventory_df = get_inventory_data()

    monthly_sales = monthly_sales_summary(sales_df).to_string()
    yearly_sales = yearly_sales_summary(sales_df).to_string()
    profit = profit_loss_analysis(sales_df, expense_df)
    top_products = top_selling_products(sales_df).to_string()
    low_stock = low_stock_alert(inventory_df).to_string()

    context = f"""
    You are a business analytics assistant for Radhe Krishn Enterprises, 
    a footwear manufacturing and wholesale company based in Delhi.

    Here is the current business data:

    Monthly Sales Summary:
    {monthly_sales}

    Yearly Sales Summary:
    {yearly_sales}

    Profit and Loss:
    Total Sales: {profit['total_sales']} {profit['currency']}
    Total Expenses: {profit['total_expenses']} {profit['currency']}
    Net Profit: {profit['profit']} {profit['currency']}

    Top Selling Products:
    {top_products}

    Low Stock Items:
    {low_stock}

    Answer the user's business questions based on this data only.
    Give clear and concise answers in simple language.
    """
    return context

def ask_chatbot(user_question):
    context = build_business_context()
    prompt = f"{context}\n\nUser Question: {user_question}"
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Chatbot error: {str(e)}"
