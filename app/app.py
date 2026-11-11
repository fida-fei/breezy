import streamlit as st
import pandas as pd
import joblib

# Load weather dataset
df = pd.read_csv("data/weather_data.csv")

# Convert time column
df["time"] = pd.to_datetime(df["time"])

# Load trained wind speed model
saved_model = joblib.load("models/wind_speed_model.pkl")

model = saved_model["model"]
features = saved_model["features"]

# Prepare features for wind speed prediction
df["hour"] = df["time"].dt.hour
df["month"] = df["time"].dt.month

df["previous_hour_wind"] = df["wind_speed_10m"].shift(1)
df["wind_2_hours_ago"] = df["wind_speed_10m"].shift(2)
df["wind_3_hours_ago"] = df["wind_speed_10m"].shift(3)

# Predict wind speed for the next hour
latest_features = df[features].iloc[[-1]]
predicted_wind_speed = model.predict(latest_features)[0]

st.subheader("Wind Speed Prediction")
prediction_time = df["time"].iloc[-1] + pd.Timedelta(hours=1)

st.caption(
    f"Prediction for: {prediction_time.strftime('%d %b %Y, %I:%M %p')}"
)
st.metric(
    "Predicted Wind Speed (Next Hour)",
    f"{predicted_wind_speed:.1f} km/h"
)

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
# Wind speed history
st.subheader("Wind Speed History")

recent_data = df.tail(48).set_index("time")

st.line_chart(
    recent_data["wind_speed_10m"],
    y_label="Wind Speed (km/h)",
    x_label="Time"
)
# Wind direction distribution
st.subheader("Wind Direction Distribution")

directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

direction_labels = (
    ((df["wind_direction_10m"] + 22.5) % 360) // 45
).astype(int).map(dict(enumerate(directions)))

direction_counts = direction_labels.value_counts().reindex(
    directions, fill_value=0
)

st.bar_chart(
    direction_counts,
    y_label="Number of observations",
    x_label="Wind Direction"
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