import yfinance as yf
import streamlit as st
import pandas as pd

st.set_page_config(page_title="SOUN AI Stock Bot", layout="centered")

st.title("🤖 SOUN Real-Time Stock Bot")

symbol = "SOUN"
stock = yf.Ticker(symbol)

hist = stock.history(period="5d", interval="5m")
price = hist["Close"].iloc[-1]

ma20 = hist["Close"].rolling(20).mean().iloc[-1]
ma50 = hist["Close"].rolling(50).mean().iloc[-1]

signal = "HOLD"
if ma20 > ma50:
    signal = "BUY"
elif ma20 < ma50:
    signal = "SELL"

st.metric("💲 Current Price", f"${price:.2f}")
st.metric("📊 Signal", signal)

st.subheader("Price Chart")
st.line_chart(hist["Close"])

st.subheader("Moving Averages")
st.line_chart(hist[["Close"]].rolling(20).mean())

st.caption("Data: Yahoo Finance | SOUN AI Bot")
