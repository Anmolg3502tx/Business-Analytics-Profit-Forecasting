import sqlite3
from config import DATABASE_PATH

def create_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            product_name TEXT,
            category TEXT,
            quantity INTEGER,
            unit_price REAL,
            total_amount REAL,
            retailer_name TEXT,
            payment_status TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            category TEXT,
            stock_quantity INTEGER,
            unit_cost REAL,
            last_updated TEXT,
            days_in_stock INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            description TEXT,
            amount REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_number TEXT,
            date TEXT,
            retailer_name TEXT,
            total_amount REAL,
            gst_amount REAL,
            payment_status TEXT
        )
    ''')

    conn.commit()
    conn.close()
    print("Database tables created successfully.")
