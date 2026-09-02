import pandas as pd

# Load weather data
df = pd.read_csv("data/weather_data.csv")

# Calculate statistics
print("===== BREEZY WEATHER SUMMARY =====")
print()

print("Average wind speed:",
      round(df["wind_speed_10m"].mean(), 2), "km/h")

print("Minimum wind speed:",
      round(df["wind_speed_10m"].min(), 2), "km/h")

print("Maximum wind speed:",
      round(df["wind_speed_10m"].max(), 2), "km/h")

print()

print("Average temperature:",
      round(df["temperature_2m"].mean(), 2), "°C")

print("Average humidity:",
      round(df["relative_humidity_2m"].mean(), 2), "%")

print("Average pressure:",
      round(df["pressure_msl"].mean(), 2), "hPa")

print()

print("Wind direction range:",
      round(df["wind_direction_10m"].min(), 2),
      "° to",
      round(df["wind_direction_10m"].max(), 2),
      "°")