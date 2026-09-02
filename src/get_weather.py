import requests
import pandas as pd

# Kozhikode coordinates
latitude = 11.2588
longitude = 75.7804

# Historical data from the last 6 months
url = "https://archive-api.open-meteo.com/v1/archive"

params = {
    "latitude": latitude,
    "longitude": longitude,
    "start_date": "2026-03-01",
    "end_date": "2026-08-31",
    "hourly": [
        "temperature_2m",
        "relative_humidity_2m",
        "pressure_msl",
        "wind_speed_10m",
        "wind_direction_10m"
    ],
    "timezone": "auto"
}

# Get weather data
response = requests.get(url, params=params)

print("Downloading historical weather data...")

if response.status_code == 200:

    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data["hourly"])

    # Save data
    df.to_csv("data/weather_data.csv", index=False)

    print("Historical weather data downloaded successfully!")
    print("Number of records:", len(df))
    print("Saved to: data/weather_data.csv")

else:
    print("Something went wrong.")
    print("Status code:", response.status_code)