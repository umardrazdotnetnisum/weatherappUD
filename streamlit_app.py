# streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime, timedelta

# ----- DUMMY DATA GENERATOR -----
def generate_dummy_weather(days=30):
    base = datetime.today()
    data = []

    for i in range(days):
        date = base - timedelta(days=i)
        data.append({
            "date": date.strftime("%Y-%m-%d"),
            "temperature": round(random.uniform(20, 40), 1),
            "humidity": random.randint(30, 90),
            "wind_speed": round(random.uniform(1, 10), 1)
        })

    return pd.DataFrame(data[::-1])  # reverse to have oldest first

# ----- PLOT FUNCTION -----
def plot_weather(df):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["date"], df["temperature"], label="Temperature (°C)", marker='o', color='red')
    ax.plot(df["date"], df["humidity"], label="Humidity (%)", marker='x', color='blue')
    ax.plot(df["date"], df["wind_speed"], label="Wind Speed (m/s)", marker='s', color='green')

    ax.set_xlabel("Date")
    ax.set_ylabel("Values")
    ax.set_title("Weather Trends (Dummy Data)")
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# ----- STREAMLIT UI -----
st.set_page_config(page_title="Dummy Weather Dashboard", layout="centered")

st.title("🌤️ Dummy Weather Dashboard")
st.write("This dashboard shows weather data for the past 30 days (generated randomly).")

# Generate and show dummy data
df = generate_dummy_weather()
st.dataframe(df)

# Plotting
st.subheader("📈 Weather Trend Over Time")
plot_weather(df)
