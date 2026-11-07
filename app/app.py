import streamlit as st
import pandas as pd

# Load weather dataset
df = pd.read_csv("data/weather_data.csv")

# Convert time column
df["time"] = pd.to_datetime(df["time"])

# Page configuration
st.set_page_config(
    page_title="Breezy | Wind Intelligence",
    page_icon=" ",
    layout="wide"
)

# Main heading
st.title("Breezy")
st.subheader("Understand the wind. Predict its movement.")

st.write(
    "Breezy is a wind intelligence application "
    "that analyses weather data and predicts wind conditions."
)
# Latest weather information
latest = df.iloc[-1]

st.subheader("Weather Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Temperature",
        f"{latest['temperature_2m']:.1f} °C"
    )

with col2:
    st.metric(
        "Wind Speed",
        f"{latest['wind_speed_10m']:.1f} km/h"
    )

with col3:
    st.metric(
        "Wind Direction",
        f"{latest['wind_direction_10m']:.0f}°"
    )
    
# Welcome section
st.info("Welcome to Breezy! Your wind prediction dashboard is coming to life.")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.write("Dashboard")
st.sidebar.write("Wind Analysis")
st.sidebar.write("Predictions")

# Footer
st.divider()
st.caption("Breezy | Wind Intelligence Project")