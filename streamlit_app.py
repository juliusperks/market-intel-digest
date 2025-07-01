import streamlit as st
import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
DB_URL = os.getenv("DATABASE_URL")

st.title("Market Intel Digest")

conn = psycopg2.connect(DB_URL)
cur = conn.cursor()

cur.execute("""
    SELECT ticker, date, open, high, low, close, volume
    FROM market_data
    ORDER BY date DESC, ticker
    LIMIT 100
""")

rows = cur.fetchall()
df = pd.DataFrame(rows, columns=["Ticker", "Date", "Open", "High", "Low", "Close", "Volume"])
st.dataframe(df)

cur.close()
conn.close()


ticker = st.selectbox("Select a Ticker", df["Ticker"].unique())
filtered = df[df["Ticker"] == ticker].sort_values("Date")

st.line_chart(filtered.set_index("Date")[["Close"]])
