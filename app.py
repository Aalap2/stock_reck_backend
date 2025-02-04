import streamlit as st
import requests

# Backend URL (Replace with your Render FastAPI URL)
BASE_URL = "https://stock-reck-backend.onrender.com"

# App Title
st.set_page_config(page_title="Stock Market Recommendation", layout="wide")
st.title("📈 Stock Market Recommendation System")

# User Signup Form
st.subheader("📝 User Information")
col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("👤 Enter your name")
with col2:
    age = st.number_input("🎂 Enter your age", min_value=18, max_value=100, step=1)
with col3:
    capital = st.number_input("💰 Investment Capital", min_value=1000, step=500)

risk_capacity = st.radio("⚡ Select Risk Capacity", ["Low", "Medium", "High"], horizontal=True)

if st.button("🚀 Sign Up", use_container_width=True):
    user_data = {"name": name, "age": age, "capital": capital, "risk_capacity": risk_capacity}
    response = requests.post(f"{BASE_URL}/signup", json=user_data)
    
    if response.status_code == 200:
        api_key = response.json()["api_key"]
        st.session_state["api_key"] = api_key
        st.success(f"🎉 Signup Successful! Your API Key: `{api_key}`")
    else:
        st.error("❌ Signup Failed! Try Again.")

# Check if API Key Exists
if "api_key" in st.session_state:
    api_key = st.session_state["api_key"]
    
    # Stock Data Section
    st.subheader("📊 Stock Data")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        ticker = st.text_input("🔎 Enter Stock Ticker (e.g., RELIANCE, TCS)")
    with col2:
        if st.button("📈 Get Stock Data", use_container_width=True):
            headers = {"Authorization": api_key}
            response = requests.get(f"{BASE_URL}/nse/stock/{ticker}", headers=headers)
            
            if response.status_code == 200:
                stock_data = response.json()["data"]
                st.json(stock_data)
            else:
                st.error("❌ Failed to fetch stock data.")

    # Get Stock Recommendations
    if st.button("🎯 Get Recommendations", use_container_width=True):
        headers = {"Authorization": api_key}
        response = requests.post(f"{BASE_URL}/recommend", json=user_data, headers=headers)
        
        if response.status_code == 200:
            recommendations = response.json()["recommendations"]
            st.success("✅ Recommended Stocks for You:")
            for stock in recommendations:
                st.write(f"- {stock}")
        else:
            st.error("❌ Failed to fetch recommendations.")
