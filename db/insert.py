import os
import psycopg2
from dotenv import load_dotenv

from parse.parser import MarketEntry

load_dotenv()
DB_URL = os.getenv("DATABASE_URL")

def insert_all(entries):
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()

    cur.executemany("""
        INSERT INTO market_data (ticker, date, open, high, low, close, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, [
        (e.ticker, e.date, e.open, e.high, e.low, e.close, e.volume)
        for e in entries
    ])

    conn.commit()
    cur.close()
    conn.close()
