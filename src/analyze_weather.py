import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt

# Load our weather data
df = pd.read_csv("data/weather_data.csv")

# Convert time from text into actual dates
df["time"] = pd.to_datetime(df["time"])

# Create the graph
plt.figure(figsize=(12, 5))

plt.plot(df["time"], df["wind_speed_10m"])

plt.title("Breezy - Wind Speed Over Time")
plt.xlabel("Time")
plt.ylabel("Wind Speed (km/h)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("data/wind_speed_graph.png")
print("Graph saved successfully!")